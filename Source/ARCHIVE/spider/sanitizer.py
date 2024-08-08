import sys, os
import glob
from urllib.parse import urlparse

import warcio
from warcio.archiveiterator import ArchiveIterator
from warcio.warcwriter import WARCWriter

from crawler import CustomProxyMiddleware as P

def main(args):
	source_dir = args[1]
	kind = args[2]
	dedup_uri = 'dedup-uri' == args[3]

	if not kind in ['*', 'images', 'media', 'styles', 'files']:
		raise ValueError(kind)

	for f in glob.glob(os.path.join(source_dir, "*.warc")):
		victims = set()
		known_ids = dict()
		print(f"Processing {f:s}")
		fnew = f.replace(".warc", ".warc.clean")
		with open(f, 'rb') as stream:
			for record in ArchiveIterator(stream):
				_id = record.rec_headers.get_header('WARC-Record-ID')
				if _id in known_ids:
					known_ids[_id] += 1
				else:
					known_ids[_id] = 1

				if not record.rec_type in ['response', 'revisit']: continue

				_status_code = int(record.http_headers.get_statuscode())//100
				if 4 == _status_code:
					victims.add(_id)
					continue
				if 5 == _status_code:
					victims.add(_id)
					continue

				uri = record.rec_headers.get_header('WARC-Target-URI')
				selector = P.categorise_url(uri)
				if selector != kind:
					victims.add(_id)
					continue

		duplicated_ids = set([i for i in known_ids if 1 != known_ids[i]])
		print("","Found {:d} duplicated records.".format(len(duplicated_ids)), sep="\t")
		print("","{:d} unwanted records will be removed.".format(len(victims)), sep="\t")

		surviving_ids = set()
		orphaned_ids = set()
		deduplicated_ids = set()
		known_uris = dict()
		deduplicated_uris = set()
		with open(f, 'rb') as fin, open(fnew, 'wb') as fout:
			writer = WARCWriter(fout, gzip=False)
			for record in ArchiveIterator(fin):
				_id = record.rec_headers.get_header('WARC-Record-ID')
				concurrent_id = record.rec_headers.get_header('WARC-Concurrent-To', None)

				if _id in victims: continue
				if _id in surviving_ids:
					deduplicated_ids.add(_id)
					continue
				if concurrent_id and (concurrent_id in victims or concurrent_id not in surviving_ids):
					orphaned_ids.add(_id)
					continue

				this_type = record.rec_headers.get_header('WARC-Type')
				this_uri = record.rec_headers.get_header('WARC-Target-URI')
				if dedup_uri:
					if this_type in known_uris and this_uri in known_uris[this_type]:
						deduplicated_uris.add(this_uri)
						continue
					else:
						deduplicated_uris.add(this_uri)
						if this_type not in known_uris: known_uris[this_type] = set()
						known_uris[this_type].add(this_uri)

				writer.write_record(record)
				surviving_ids.add(_id)

		print("","{:d} records survived, {:d} were purged due becoming orphans.".format(len(surviving_ids), len(orphaned_ids)), sep="\t")
		if dedup_uri: print("","{:d} URIS were deduplicated.".format(len(deduplicated_uris)), sep="\t")

		with open(f+".report", "w") as freport:
			print("{:d} unwanted records were removed : {:s}".format(len(victims), repr(victims)), file=freport)
			print("", file=freport)
			print("{:d} records were deduplicated : {:s}".format(len(deduplicated_ids), repr(deduplicated_ids)), file=freport)
			print("", file=freport)
			print("{:d} records became orphaned and were purged : {:s}".format(len(orphaned_ids), repr(orphaned_ids)), file=freport)
			print("", file=freport)
			if dedup_uri:
				print("{:d} URIs were deduplicated : {:s}".format(len(deduplicated_uris), repr(deduplicated_uris)), file=freport)
				print("", file=freport)
			print("{:d} records survived the ordeal : {:s}".format(len(surviving_ids), repr(surviving_ids)), file=freport)

		creation_time = os.path.getctime(f)
		modification_time = os.path.getmtime(f)
		os.utime(fnew, (creation_time, modification_time))

if '__main__' == __name__:
	main(sys.argv)
	#main(["", "/Users/lisias/Workspaces/KSP-Forum/GIT/KSP-Forum-Preservation-Project/torrent/KSP-Forum-Preservation-Project", "content"])
