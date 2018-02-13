# -*- coding: utf-8 -*-
'''
Uses Scrapy to gather information from https://www.apple.com/retail/storelist/.
Feilds: Country, State/Region, City, Store Name, Address, Picture URL
Outputs json file containing information of all 501 apple stores.

Developer: Charles Calder
Start Date: February 10th, 2018
'''

import scrapy
import Canopy.geocode
from Canopy.items import AppleItem

class AppleStoreSpider(scrapy.Spider):
	'''Basic spider class'''
	# Used for calling spider with scrapy
	name = 'apple'
	# Domain in which spider is allowed to move
	allowed_domains = ['apple.com']
	# Url to be joined with extracted urls
	base_url = 'https://www.apple.com'
	# Url on which the spider starts
	start_urls = ['https://www.apple.com/retail/storelist/']
	geo = Canopy.geocode.Geo()

	def parse(self, response):
		# Gather and organize response data from website
		countries = response.xpath("//div[contains(@id, 'stores')]") # List of country elements
		for country in countries:
			sites = country.xpath('*//a/@href').extract() # List of domains to be joined with base
			for site in sites:
				if site is not None:
					# If the new site exists, analyze the store page with a store specific method
					url = str.format("{}{}", self.base_url, site)
					yield scrapy.Request(url, callback=self.parse_store_page)

	def parse_store_page(self, response):
		# Sort data for store pages into AppleItem
		def xpath_extract(element, class_id, key):
			# Turn a few values into an item key-value pair (for readability)
			query = str.format("//{}[contains(@class, '{}')]/text()", element, class_id)
			data = response.xpath(query).extract_first()
			# This allows us to only see non-null key-value pairs
			if data is not None:
				item[key] = data.encode('utf8').strip()

		# Create apple item for data storage
		item = AppleItem()

		# Fill apple item with relevant information
		xpath_extract("a", "ac-gf-footer-locale-link", "country") # Country
		xpath_extract("span", "store-street", "address") # Street address
		xpath_extract("span", "store-region", "region")	# Region/State
		xpath_extract("span", "store-locality", "city") # City
		xpath_extract("h1", "headline", "name") # Name of store

		# Image cannot be extracted, instead find it by adding text to end of response url
		item['img'] = str.format("{}{}", response.request.url, "images/hero_medium.jpg")
		
		# Get geocoordinates from item address
		coords = self.geo.locate(item)
		if coords is not None:
			item['lat'] = coords[0]
			item['lng'] = coords[1]
		yield item
