# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstituteItem(scrapy.Item):
    inst_name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()

class DepartmentItem(scrapy.Item):
    dep_name = scrapy.Field()
    url = scrapy.Field()
    institute = scrapy.Field()