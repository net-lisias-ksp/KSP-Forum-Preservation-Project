import os
from urllib.parse import urlparse

class CustomProxyMiddleware(object):
	def __init__(self):
		self.proxy = dict()
		self.proxy['*'] = 'http://steamdeck:8088'

	def process_request(self, request, spider):
		if 'proxy' not in request.meta:
			path = urlparse(request.url).path
			ext = os.path.splitext(path)[1]
			selector = ext[1:].lower()
			if not selector in self.proxy:
				selector = '*'
			request.meta['proxy'] = self.proxy[selector]
		print ("** SELECTED", request.meta['proxy'])

	def get_proxy(self):
		return self.proxy['*']
