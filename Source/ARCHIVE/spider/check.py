import sys, os
import glob
from urllib.parse import urlparse

import warcio
from warcio.archiveiterator import ArchiveIterator
from warcio.warcwriter import WARCWriter

from crawler import CustomProxyMiddleware as P

def main(args):
	source_dir = args[1]

	for f in glob.glob(os.path.join(source_dir, "*.warc")):
		known_ids = dict()
		concurrents = set()
		print(f"Processing {f:s}")
		fnew = f.replace(".warc", ".warc.clean")
		with open(f, 'rb') as stream:
			for record in ArchiveIterator(stream):
				_id = record.rec_headers.get_header('WARC-Record-ID')
				if _id in known_ids:
					known_ids[_id] += 1
				else:
					known_ids[_id] = 1

				concurrent_id = record.rec_headers.get_header('WARC-Concurrent-To')
				concurrents.add(concurrent_id)

		weird_ones = set([i for i in known_ids if 1 != known_ids[i]])
		print("", "Found {:d} weird records: {:s}".format(len(weird_ones), repr(weird_ones)), sep="\t")

		orphaned_concurrents = set([x for x in concurrents if x not in known_ids])
		print("", "Found {:d} orphaned concurrent records: {:s}".format(len(orphaned_concurrents), repr(orphaned_concurrents)), sep="\t")

if '__main__' == __name__:
	main(sys.argv)
	#main(["", "/Users/lisias/Workspaces/KSP-Forum/GIT/KSP-Forum-Preservation-Project/torrent/KSP-Forum-Preservation-Project", "content"])
