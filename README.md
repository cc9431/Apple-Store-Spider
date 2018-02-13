# Apple Store Spider

Charles Calder

February 10th, 2018

The store_spider.py file runs on python 3.6, and uses Scrapy 1.5.0 and googlemaps (Python client for Google API). This spider will scrape information from the webpage "https://www.apple.com/retail/storelist/" and return a json file containing relevant information on all 501 Apple stores.

## TODO
* Clean up files 
	* middleware.py, pipelines.py, etc.
* Google Maps API
	* Better way to call api?
	* Better way to find location?