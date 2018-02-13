'''
Helper script for finding latitude
and longitude based on address.
'''

import googlemaps
from items import AppleItem

class Geo(object):
	'''Geocoding class'''
	client = googlemaps.Client(key="AIzaSyAvN5JuxoIToH_6-wHc5M8Ky9LTTc2Xckg")

	def lat_long(self, address):
		'''Turn address to geographic coordinates'''
		return_list = self.client.geocode(address)
		json = return_list[0]
		geocoords = json['geometry']['location']
		lat = geocoords['lat']
		lng = geocoords['lng']
		return lat, lng

	def convert(self, item):
		'''Turn AppleItem into usable address'''
		pass

# TEST
# g = Geo()
# lat, lng = g.lat_long("126 State Street, Brooklyn, NY")
# print "latitude:", lat 
# print "longitude:", lng