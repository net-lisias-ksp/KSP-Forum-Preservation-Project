from typing import Iterable

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import crawler

class MySpider(CrawlSpider):
	name = 'forum.kerbalspaceprogram.com'
	allowed_domains = ['forum.kerbalspaceprogram.com']
	start_urls = ['https://forum.kerbalspaceprogram.com/']
	custom_settings = {
		'AUTOTHROTTLE_ENABLED': True,
		'AUTOTHROTTLE_START_DELAY': 1,
		'AUTOTHROTTLE_MAX_DELAY': 300,	# 5 Minutes
		'RETRY_TIMES': 1024,
		'DOWNLOADER_MIDDLEWARES': {
			'crawler.CustomProxyMiddleware': 350,
		},
		'USER_AGENT': "Mozilla/5.0 (Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
		'DEFAULT_REQUEST_HEADERS': {
			"Accept-Encoding": "identity"
		}
	}

	rules = (
		Rule(LinkExtractor(), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		print(response.url)
		return {'url': response.url}