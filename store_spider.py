'''
Uses Scrapy to gather information from https://www.apple.com/retail/storelist/.
Feilds: Country, State/Region, City, Store Name, Address, Picture URL
Outputs json file containing information of all apple stores.

Charles Calder
February 10th, 2018

NOTE: This script runs on python 3.6
'''

import scrapy

class AppleStoreSpider(scrapy.Spider):
	'''Basic spider class'''
	name = 'Apple Spider'
	urls = ['https://www.apple.com/retail/storelist/']

	def crawl(self, response):
		# Gather and organize response data from website
		pass

