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
		'''Gather and organize response data from website'''
		# Get list of country elements from webpage data
		countries = response.xpath("//div[contains(@id, 'stores')]")
		for country in countries:
			# Get list of domains to be joined with base_url
			sites = country.xpath('*//a/@href').extract()
			for site in sites:
				# If the new site exists,
				# analyze the store page with a store specific method
				url = str.format("{}{}", self.base_url, site)
				yield scrapy.Request(url, callback=self.parse_store_page)

	def parse_store_page(self, response):
		'''Organize data from store pages into AppleItems'''
		def xpath_extract(element, class_id, key):
			'''Turn values into an item key-value pair'''
			query = str.format("//{}[contains(@class, '{}')]/text()", element, class_id)
			data = response.xpath(query).extract_first()
			# This allows us to only see non-null key-value pairs
			if data is not None:
				item[key] = data.encode('utf8').strip()

		# Create apple item for data storage
		item = AppleItem()

		# Country
		xpath_extract("a", "ac-gf-footer-locale-link", "country")
		# Street address
		xpath_extract("span", "store-street", "address")
		# Region/State
		xpath_extract("span", "store-region", "region")
		# City
		xpath_extract("span", "store-locality", "city")
		# Name of store
		xpath_extract("h1", "headline", "name")

		# Image cannot be extracted from store page HTML
		# Instead find it by adding text to end of response url
		item['img'] = str.format("{}{}", response.request.url, "images/hero_medium.jpg")

		# Use google api geocode to find store coordinates
		coords = self.geo.locate(item)
		if coords is not None:
			item['lat'] = coords[0]
			item['lng'] = coords[1]

		yield item
