'''
Uses Scrapy to gather information from https://www.apple.com/retail/storelist/.
Feilds: Country, State/Region, City, Store Name, Address, Picture URL
Outputs json file containing information of all apple stores.

Charles Calder
February 10th, 2018

NOTE: This script runs on python 3.6
'''

#import scrapy_splash
import scrapy
from Canopy.items import AppleItem

class AppleStoreSpider(scrapy.Spider):
	'''Basic spider class'''
	name = 'apple'
	allowed_domains = ['apple.com']
	base_url = 'https://www.apple.com'
	start_urls = ['https://www.apple.com/retail/storelist/']

	def parse(self, response):
		# Gather and organize response data from website
		countries = response.xpath("//div[contains(@id, 'stores')]")
		for country in countries:
			sites = country.xpath('*//a/@href').extract()
			for site in sites:
				if site is not None:
					url = str.format("{}{}", self.base_url, site)
					yield scrapy.Request(url, callback=self.parse_store_page)

	def parse_store_page(self, response):
		def css_extract(section, text, key):
			query = str.format("//{}[contains(@class, '{}')]/text()", section, text)
			string = response.xpath(query).extract_first()
			if string is not None:
				item[key] = string.strip()

		item = AppleItem()
		css_extract("h1", "headline", "name")
		css_extract("span", "store-region", "region")
		css_extract("span", "store-locality", "city")
		css_extract("span", "store-street", "address")
		css_extract("a", "ac-gf-footer-locale-link", "country")
		#item['img'] = working on it :)
		
		# postal_code = css_extract("span", "store-postal-code", )
		# if postal_code is not None:
		# 	if item['region'] is None:
		# 		item['region'] = postal_code
		# 	else:
		# 		item['region'] = str.format("{}, {}", item['region'], postal_code)
		yield item
