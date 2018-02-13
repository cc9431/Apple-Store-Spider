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
		return_list = self.client.geocode(address)
		if len(return_list) > 0:
			json = return_list[0]
			geocoords = json['geometry']['location']
			lat = geocoords['lat']
			lng = geocoords['lng']
			return lat, lng
		return None

	def convert(self, item):
		'''Turn AppleItem into usable address'''
		address = item['name'].decode('utf8')
		# for value in item.values():		# Still possible
		# 	address = str.format("{}, {}", address, value)
		return address

########################################## TEST ##########################################
# g = Geo()

# item = AppleItem()
# item['name'] = "Apple 가로수길"

# coords = g.locate(item)

# print "latitude:", coords[0]
# print "longitude:", coords[1]