# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()
    

class InstituteItem(scrapy.Item):
    inst_name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()

class DepartmentItem(scrapy.Item):
    dep_name = scrapy.Field()
    url = scrapy.Field()
    institute = scrapy.Field()

class Lab6Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
