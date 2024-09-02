# KSP's Forum Preservation Project :: Tools

This document aims to be a "cheat-sheet" with quick hints for many different tasks needed to carry on the project.

See [Theory](./Theory.md) for a thoughtfully description.


## Downloading IA's forum.kerbalspaceprogram.com_202305

To anyone willing to download the Internet Archive data, this dataset doesn't have a torrent, unfortunately.

So I made this little script to download that huge basket of bytes using wget with the option to recover the downloads if things goes south in the process. Worst case scenario, you run the script again, no data loss. 

Here: [download-forum.kerbalspaceprogram.com_202305](../Source/bash/download-forum.kerbalspaceprogram.com_202305.sh)


## Dumping a URL from IA's into a local WARC

Source: https://github.com/openzim/warc2zim/issues/95#issuecomment-1166366024

Here: [wayback_dl.sh](../Source/bash/wayback_dl.sh)


## Extracting all URLs archived from the WARC files

```
cat *.warc | grep -a "WARC-Target-URI" | sed 's/WARC-Target-URI: //' | dos2unix | sort | uniq > uri.txt

```

## Listing all images from the `<img src="">` tags from the html archived on the WARC files.

```
cat *.warc | grep -Poa '<img[^>]*src="\K[^"]*(?=")' | dos2unix | sort | uniq > imgs.txt
```

## Listing all `Content-Type`s from the WARC files.

```
cat *.warc | grep -ae "^Content-Type: " | sed '/msgtype/d' | dos2unix | sort | uniq
```

### Summarising them

```
for f in *.warc ; do echo $f; cat $f | grep -a "^Content-Type:" | sort | uniq -c ; echo ""; done
```

## Summarising all archived URI's from the WARC files.

```
for f in *.warc ; do echo $f; cat $f | grep -a "^WARC-Target-URI:" | sort | uniq -c ; echo ""; done
```

Note: each URI **must** have a **even** count, otherwise the WARC file is damaged. Divide the count by 2 to get how many times that URL is present on the WARC file.


## Internet Archive

The following commandline will dump the CDX for the pages archived by `archive.org` from the Forum. It's a good benchmark to compare with our own results.

> ATTENTION: This tool is currently untested!

```
curl http://web.archive.org/cdx/search/cdx?url=forum.kerbalspaceprogram.com/* > ia.forum-kerbalspaceprogram-com.cdx
```

And the following will extract the URLs (removing duplicates) from the CDX above:

```
cat ia.forum-kerbalspaceprogram-com.cdx | cut -d' ' -f 3 | sort | uniq > ia.uri.txt

```


## `pywb` a Python Web Archiving Toolkit for replay and recording of web archives

wip


## `scrappy`

	scrapy runspider doit.py -s JOBDIR=./forum.kerbalspaceprogram.com


### `lrzip` the best compression tool available today.

To compress all WARC files with maximum compression, preserving the original:

	lrz -z --best --keep *.warc
	
	for f in *.warc; do lrz -z --best --keep $f ; touch -r ${f/.lrz/} $f ; done

To decompress

	lrz --decompress --keep *.lrz

**ATTENTION**: this thing is **ssslloooowwwww**, but it gives us the best compression ratio available nowadays.

We are dealing with huge data files that will be shared between many, many people. This is going to save a lot of money for AWS users.

### Rebuilding the ignore files

do a `./sanitize_all` , and then

	cat forum.kerbalspaceprogram.com-2024*.warc.clean | grep -a "^WARC-Target-URI: " | sed "s/^WARC-Target-URI: //g" | sed "s/^\(.+\)#?.+/\1/g" | sort | uniq | dos2unix > <[filename]>.txt

where `<[filename]>` is:

* `crawled_urls` for the list of urls that where already crawled on the current task force. Do it on the `-content` collection.
* `ignore-list` for the list of the urls that should never be crawled again (this list is committed). Do it on the `-files` and `-images` collections.


## `transmission-daemon` as (command line) torrent client

wip

	transmissioncli -n folder.name.here -a udp://tracker.example.com:80 -w /home/user/test.torrent

hint: mutable torrents (BEP46)


### Signing the files to prevent tampering.

wip

	f=[file_to_sign]
	ssh-keygen -Y sign -f [keypath] -n $f.sig $f


### Verifying file signatures

	for f in *.lrz; do ssh-keygen -Y verify -f ./allowed_signers -I net.lisias.ksp-Forum-Preservation-Project -n $f.sig -s $f.sig < $f ; done


## redis

### export

	redis-export -u "redis://macmini62:6379/0/pywb:forum.kerbalspaceprogram.com:cdxj" "pywb:forum.kerbalspaceprogram.com" redis.dump.json
	

