# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JicheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    models = scrapy.Field()
    capacity = scrapy.Field()
    price = scrapy.Field()
    payload = scrapy.Field()
    link = scrapy.Field()
