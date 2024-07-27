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
	IMAGES_EXT = set(['gif', 'png', 'jpg', 'jpeg', 'webp', 'svg'])
	MEDIA_EXT = set(['mov', 'mp4', 'mp3', 'mp2', 'avi'])
	STYLES_EXT = set(['css', 'woff', 'woff2', 'js'])

	def __init__(self):
		self.proxy = dict()
		self.proxy['*'] = 'http://steamdeck:8080'
		self.proxy['images'] = 'http://steamdeck:8082'
		self.proxy['media'] = self.proxy['images']
		self.proxy['styles'] = 'http://steamdeck:8083'

	def process_request(self, request, spider):
		if 'proxy' not in request.meta:
			parsed_url = urlparse(request.url)
			if parsed_url.path.startswith('/applications/core/interface/file/cfield.php'):
				query = dict([(k,v) for k,v in [x.split('=') for x in parsed_url.query.split('&')]])
				ext = os.path.splitext(query['path'])[1].lower()
			else:
				ext = os.path.splitext(parsed_url.path)[1].lower()
			selector = '*'
			if ext in CustomProxyMiddleware.IMAGES_EXT:
				selector = 'images'
			elif ext in CustomProxyMiddleware.STYLES_EXT:
				selector = 'styles'
			elif ext in CustomProxyMiddleware.MEDIA_EXT:
				selector = 'media'
			elif '.amazonaws.com' in parsed_url.netloc:
				selector = 'images'
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
