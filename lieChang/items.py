# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiechangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comments = scrapy.Field()
    commentTime = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()
    # pass
