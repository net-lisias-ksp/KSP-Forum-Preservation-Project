import sys, os
import glob
import warcio
from warcio.archiveiterator import ArchiveIterator

def main(args):
	source_dir = args[1]
	for f in glob.glob(os.path.join(source_dir, "*.warc")):
		with open(f, 'rb') as stream:
			for record in ArchiveIterator(stream):
				if 'response' != record.rec_type: continue
				status = int(record.http_headers.get_statuscode())
				if (status//100) < 4: continue
				if status in [403, 404]: continue
				print(record.rec_headers.get_header('WARC-Date'), record.http_headers.statusline, sep="\t")

if '__main__' == __name__:
	main(sys.argv)
