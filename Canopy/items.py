import scrapy


class AppleItem(scrapy.Item):
    country = scrapy.Field()
    region  = scrapy.Field()
    city    = scrapy.Field()
    name    = scrapy.Field()
    address = scrapy.Field()
    img     = scrapy.Field()
    lat     = scrapy.Field()
    lng     = scrapy.Field()
