import sys, os
import glob
import re
import warcio
from warcio.archiveiterator import ArchiveIterator

def main(args):
	source_dir = args[1]
	substring = bytes(args[2], 'utf-8')
	regex_src = bytes(args[3], 'utf-8')
	regex = re.compile(regex_src)
	for f in glob.glob(os.path.join(source_dir, "*.warc")):
		print("# ** {:s}".format(str(f)))
		hits = 0
		with open(f, 'rb') as stream:
			for record in ArchiveIterator(stream):
				if 'response' != record.rec_type: continue
				status = int(record.http_headers.get_statuscode())
				if (status//100) != 2: continue
				content = record.content_stream().read()
				if substring in content:
					r = regex.search(content)
					if r:
						s = str(r.group(1), 'utf-8')
						print(record.rec_headers.get_header('WARC-Target-URI'), record.rec_headers.get_header('WARC-Date'), s, record.http_headers.statusline, sep="\t")
						hits += 1
		if hits:
			print("# Found {:d} occurences.".format(hits))
			print("#")

if '__main__' == __name__:
	main(sys.argv)
