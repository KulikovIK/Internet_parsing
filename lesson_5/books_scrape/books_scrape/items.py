# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScrapeItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    in_stock = scrapy.Field()
    product_description = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_et = scrapy.Field()
    price_it = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    number_of_reviews = scrapy.Field()
    pass

        