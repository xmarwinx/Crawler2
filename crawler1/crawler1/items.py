# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class Crawler1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    telephone_number = Field()
    detail_description = Field()

    title = Field()
    title_link = Field()
    description = Field()
    address = scrapy.Field()
    date = scrapy.Field()
    image_urls = Field()
    images = Field()

class Crawler1_detail_view_Item(Item):
    telephone_number = Field()
    detail_description = Field()
    name = Field()
    address = Field()
    detail_informations = Field()
    image_urls = Field()
    images = Field()
