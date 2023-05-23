# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ConsoleItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    shop = scrapy.Field()
    price = scrapy.Field()
    
class Mkr2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
