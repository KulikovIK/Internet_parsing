# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesParserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    pass

class AuthorParserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    born = scrapy.Field()
    description = scrapy.Field()
    pass
