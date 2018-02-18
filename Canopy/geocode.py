# -*- coding: utf-8 -*-
'''
Helper script for finding latitude
and longitude based on address.
'''

import googlemaps
from items import AppleItem

class Geo(object):
	'''Geocoding class'''
	client = googlemaps.Client(key="AIzaSyAvN5JuxoIToH_6-wHc5M8Ky9LTTc2Xckg")

	def locate(self, item):
		'''Take item, return latitude and longitude'''
		return self.lat_long(self.convert(item))

	def lat_long(self, address):
		'''Turn address to geographic coordinates'''
		# Connect to google api for geocode info
		return_list = self.client.geocode(address)
		# Make sure the return list is not empty
		if len(return_list) > 0:
			# Gather and return coordinate information
			json = return_list[0]
			geocoords = json['geometry']['location']
			lat = geocoords['lat']
			lng = geocoords['lng']
			return lat, lng
		return None

	def convert(self, item):
		'''Turn AppleItem into usable address'''
		# Since Google labels apple stores as important,
		# Location can almost always be found from only their name
		address = item['name'].decode('utf8')
		return address