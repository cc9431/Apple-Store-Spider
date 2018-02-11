'''
Uses Scrapy to gather information from https://www.apple.com/retail/storelist/.
Feilds: Country, State/Region, City, Store Name, Address, Picture URL
Outputs json file containing information of all 501 apple stores.

Developer: Charles Calder
Start Date: February 10th, 2018

NOTE: This script runs on python 3.6
'''

import scrapy
from Canopy.items import AppleItem

class AppleStoreSpider(scrapy.Spider):
	'''Basic spider class'''
	# Used for calling spider with scrapy
	name = 'apple'
	# Domain in which spider is allowed to move
	allowed_domains = ['apple.com']
	# Url to be joined with extracted urls
	base_url = 'https://www.apple.com'
	# Url the spider starts with
	start_urls = ['https://www.apple.com/retail/storelist/']

	def parse(self, response):
		# Gather and organize response data from website
		countries = response.xpath("//div[contains(@id, 'stores')]") # List of country sections
		for country in countries:
			sites = country.xpath('*//a/@href').extract() # List of domains to be joined with base
			for site in sites:
				if site is not None:
					# If the new site exists, analyze the store page with a store specific method
					url = str.format("{}{}", self.base_url, site)
					yield scrapy.Request(url, callback=self.parse_store_page)

	def parse_store_page(self, response):
		# Sort data for store pages into AppleItem
		def css_extract(section, text, key):
			# Turn a few values into an item key-value pair (for readability)
			query = str.format("//{}[contains(@class, '{}')]/text()", section, text)
			string = response.xpath(query).extract_first()
			# This allows us to only see non-null key-value pairs
			if string is not None:
				item[key] = string.strip()

		item = AppleItem()
		css_extract("span", "store-street", "address")			# Street address
		css_extract("h1", "headline", "name")					# Name of store
		css_extract("span", "store-region", "region")			# Region/State
		css_extract("a", "ac-gf-footer-locale-link", "country")	# Country
		css_extract("span", "store-locality", "city")			# City
		css_extract("" , "", "image") # item['img'] = working on it :)

		yield item
