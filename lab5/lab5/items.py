# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()
