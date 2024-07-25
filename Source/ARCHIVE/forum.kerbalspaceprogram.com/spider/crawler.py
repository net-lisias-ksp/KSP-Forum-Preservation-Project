import os, time
from urllib.parse import urlparse
import logging
import scrapy
import scrapy.pipelines.files
from scrapy.dupefilters import RFPDupeFilter

#wayback --record --proxy forum-kerbalspaceprogram-com-content  -p 8080 -b steamdeck
#wayback --record --proxy forum-kerbalspaceprogram-com-images  -p 8081 -b steamdeck
#wayback --record --proxy forum-kerbalspaceprogram-com-styles  -p 8082 -b steamdeck

class CustomProxyMiddleware(object):
	def __init__(self):
		self.proxy = dict()
		self.proxy['*'] = 'http://steamdeck:8080'
		self.proxy['gif'] = 'http://steamdeck:8081'
		self.proxy['png'] = 'http://steamdeck:8081'
		self.proxy['jpg'] = 'http://steamdeck:8081'
		self.proxy['jpeg'] = 'http://steamdeck:8081'
		self.proxy['webp'] = 'http://steamdeck:8081'
		self.proxy['svg'] = 'http://steamdeck:8081'
		self.proxy['css'] = 'http://steamdeck:8082'
		self.proxy['woff2'] = 'http://steamdeck:8082'
		self.proxy['js'] = 'http://steamdeck:8082'

	def process_request(self, request, spider):
		if 'proxy' not in request.meta:
			path = urlparse(request.url).path
			ext = os.path.splitext(path)[1]
			selector = ext[1:].lower()
			if not selector in self.proxy:
				selector = '*'
			request.meta['proxy'] = self.proxy[selector]
		logging.debug("SELECTED PROXY {:s} for {:s}".format(request.meta['proxy'], request.url))

	def get_proxy(self):
		return self.proxy['*']


class SeenURLFilter(RFPDupeFilter):
	"""A dupe filter that considers the URL"""

	def read_urls(self) -> set:
		r = set()
		with open('./ignore-list.txt', 'r') as f:
			while True:
				line = f.readline()
				if not line: break
				r.add(line)
		logging.info("Total entries read from ignore-list: {:d}".format(len(r)))
		return r

	def __init__(self, path:str = None, debug: bool = False, *, fingerprinter:[scrapy.utils.request.RequestFingerprinterProtocol] = None):
		self.urls_seen = self.read_urls()
		RFPDupeFilter.__init__(self, path)

	def request_seen(self, request):
		return False
		if request.url in self.urls_seen:
			logging.debug("Entry {:s} was ignored as duplicated.".format(request.url))
			return True
		self.urls_seen.add(request.url)


class DevNullFilesStore(scrapy.pipelines.files.FSFilesStore):
	def __init__(self, basedir:str):
		super().__init__(basedir)

	def persist_file(
		self, path:str, buf, info, meta=None, headers=None
	):
		logging.debug("Faking storing file: {:s}".format(path))

	def stat_file(self, path:str, info):
		return {"last_modified": 0, "checksum": 0}


class DevNullFilesPipeline(scrapy.pipelines.files.FilesPipeline):

	def __init__(self, store_uri, download_func=None, settings=None):
		super().__init__(store_uri, download_func=download_func, settings=settings)
		self.store = DevNullFilesStore(store_uri)
