'''
Uses Scrapy to gather information from https://www.apple.com/retail/storelist/.
Feilds: Country, State/Region, City, Store Name, Address, Picture URL
Outputs json file containing information of all apple stores.

Charles Calder
February 10th, 2018

NOTE: This script runs on python 3.6
'''

import scrapy
from Canopy.items import AppleItem

class AppleStoreSpider(scrapy.Spider):
	'''Basic spider class'''
	name = 'apple'
	allowed_domains = ['apple.com']
	start_urls = ['https://www.apple.com/retail/storelist/']

	def parse(self, response):
		# Gather and organize response data from website
		base_domain = AppleStoreSpider.allowed_domains[0]
		sites = response.xpath("//*[contains(@id, 'stores')]").xpath('*//a/@href').extract() # Get all store links
		for site in sites:
			item = AppleItem()
			item['name'] = 'HEY'
			item['address'] = site
