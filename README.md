# Apple Store Spider

Author: Charles Calder

Start Date: February 10th, 2018

## Usage
1. Install required packages

		$ pip install -r requirements.txt
2. Call spider

		$ scrapy crawl apple

## Notes
The [store_spider.py](Canopy/spiders/store_spider.py) file runs on python 3.6, and uses Scrapy 1.5.0 and googlemaps (Python client for Google API). This spider will scrape information from the webpage https://www.apple.com/retail/storelist/ and return a json file containing relevant information on all 501 Apple stores.

Output can be found in [sites.json](sites.json)