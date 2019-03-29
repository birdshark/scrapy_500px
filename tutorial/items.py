# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class GalleryItem(Item):
    collection = table = 'gallery'

    path = Field()
    size = Field()
    width = Field()
    height = Field()
    added_on = Field()
    url = Field()
    format = Field()
    pass
