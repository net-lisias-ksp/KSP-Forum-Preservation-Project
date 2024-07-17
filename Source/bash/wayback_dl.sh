#!/usr/bin/env bash
#
#
# purpose:
# this program does a prefix search on the wayback server server
# and acquires all files for a specific site which it then downloads
# and packages into a WARC file
#
# note:
# wayback cdx server docs: https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
#
#
# requires: gnu wget, jq, curl, gnu parallel, xmlstarlet, perl
#
#


#
# STAGE1: prefix search, dedupe, and retrieve all resources
#
URL="$1"

rm -rf wb_temp/*

mkdir wb_temp
mkdir wb_temp/o

curl "http://web.archive.org/cdx/search/xd?url=$URL*&fl=timestamp,original,mimetype&collapse=digest&gzip=false&filter=statuscode:200&output=json&fastLatest=true" | \
jq -c -r '.[] | (.[0]+"\t"+.[1]+"\t"+.[2])' | \
perl -ne 'print if $. > 1' | \
rg -v "wp-login.php|xmlrpc.php" > wb_temp/obj_raw_urls.txt

cat wb_temp/obj_raw_urls.txt | \
perl -ne 'push @x,[split(m{\t})]; END { print(join("\t",@$_)) for (sort { ($a->[1] cmp $b->[1]) || (-1 * ($a->[0] cmp $b->[0])) } @x);	}' | \
perl -F'\t' -ane 'BEGIN{$h={};}; print if !exists $h->{$F[1]}; $h->{$F[1]} = 1;' > wb_temp/obj_urls.txt

cat wb_temp/obj_urls.txt | \
parallel --colsep="\t" --no-notice -j4 'eval wget -nv --warc-file=wb_temp/o/{#} "https://web.archive.org/web/{1}id_/{2}" -O /dev/null'

find wb_temp/o/ -mindepth 1 -name "*.warc.gz" -exec bash -c 'zcat {} 2>>gzip_err.txt' \; > wb_temp/site.warc

cat wb_temp/site.warc | \
perl -pne 's{https?://web.archive.org/web/\d+id_/}{}; if(m{^WARC-Target-URI: <(.*)>}) {$_="WARC-Target-URI: $1\r\n";}' | \
perl -ne 'if(m{^WARC/1.0}) {print "$b" if defined($b) && $b ne "" && $b =~ m{WARC-Type: (request|response)}; $b=$_; } else {$b.=$_;} ; END { print "$b" if $b =~ m{WARC-Type: (request|response)}; };' \
> wb_temp/site2.warc

#
# STAGE2: link extraction, determining missing resources and retrieving the absent ones
#

cat wb_temp/site2.warc | perl -ne '
	BEGIN{ use File::Temp qw/tempfile/ };
	if(m{^WARC/1.0}) {
		if(defined($b) && $b ne "" && $b =~ m{Content-Type: text/html} && $b =~ m{WARC-Type: response} ) {
			($fh, $filename) = tempfile("temp_XXXX", DIR=>"wb_temp");
			print $fh $b;
			close($fh);
			print "$filename\n";
		};
		$b=$_;
	} else {
		$b.=$_;
	}
' | \
parallel --no-notice -j2 'cat {} | xmlstarlet format -H --recover 2>/dev/null | xmlstarlet sel -t -v '\''//link/@href'\'' 2>/dev/null ; rm {};'	 | \
rg -v "/wp-json/oembed|wp-login.php|http://wp.me/|^//" | \
sort | uniq > wb_temp/all_links.txt

fetch_cb() {
	curl -L -s "http://web.archive.org/cdx/search/xd?url=$1&fl=timestamp,original,mimetype&collapse=digest&gzip=false&filter=statuscode:200&output=json&fastLatest=true" | \
	jq -c -r '.[] | (.[0]+"\t"+.[1]+"\t"+.[2])' | \
	rg -v "wp-login.php|xmlrpc.php" | \
	perl -ne 'print if $. > 1' | \
	perl -ne 'push @x,[split(m{\t})]; END { print(join("\t",@$_)) for (sort { ($a->[1] cmp $b->[1]) || (-1 * ($a->[0] cmp $b->[0])) } @x);	}' | \
	perl -F'\t' -ane 'BEGIN{$h={};}; print if !exists $h->{$F[1]}; $h->{$F[1]} = 1;'
}

export -f fetch_cb

cat wb_temp/all_links.txt | \
perl -ne 's{&amp;}{&}g; print;' | \
parallel --no-notice -j8 eval fetch_cb ::: | tee wb_temp/obj2.txt

rm -f wb_temp/o2/*
mkdir wb_temp/o2/
cat wb_temp/obj_urls.txt | sort > wb_temp/r1.txt
cat wb_temp/obj2.txt	 | sort > wb_temp/r2.txt
comm -1 -3 wb_temp/r{1,2}.txt > wb_temp/r3.txt
cat wb_temp/r3.txt | \
parallel --colsep="\t" --no-notice -j4 'eval wget -nv --warc-file=wb_temp/o2/{#} "https://web.archive.org/web/{1}id_/{2}" -O /dev/null'
find wb_temp/o2/ -mindepth 1 -name "*.warc.gz" -exec bash -c 'zcat {} 2>>gzip_err.txt' \; > wb_temp/site3.warc

cat wb_temp/site2.warc wb_temp/site3.warc | \
perl -pne 's{https?://web.archive.org/web/\d+id_/}{}; if(m{^WARC-Target-URI: <(.*)>}) {$_="WARC-Target-URI: $1\r\n";}' | \
perl -ne 'if(m{^WARC/1.0}) {print "$b" if defined($b) && $b ne "" && $b =~ m{WARC-Type: (request|response)}; $b=$_; } else {$b.=$_;} ; END { print "$b" if $b =~ m{WARC-Type: (request|response)}; };' \
> wb_temp/site4.warc
