import scrapy
from lxml import etree

from ..items import QuotesParserItem as quotes_items
from ..items import AuthorParserItem as authors_items

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('//div[contains(@class, "quote")]')
        next_link = response.xpath('//nav/ul/li[contains(@class, "next")]/a/@href').get()

        if next_link:
            next_page_link = response.urljoin(next_link)
            yield response.follow(url=next_page_link, callback=self.parse)

        for xml_quote in quotes:
            text = xml_quote.xpath('./span[contains(@class, "text")]/text()').get()
            tags = xml_quote.xpath('./div[contains(@class, "tags")]/a/text()').getall()
            
            yield quotes_items(
                text=text,
                tags=str(tags)
            )
         
        for xml_quote in quotes:
            author_link = xml_quote.xpath('//small[contains(@class, "author")]/text()').get()
            author_link_page = (f"http://quotes.toscrape.com/author/{author_link.replace(' ', '-').replace('.','-').replace('--', '-')}/")
            print('*'*50)
            print(author_link_page)
            yield response.follow(url=author_link_page, callback=self.author_parser)
    
    def author_parser(self, response):
        name = response.xpath('//h3/text()').get()
        born = response.xpath('//span[contains(@class,"date")]/text()').get()
        description = response.xpath('//div[contains(@class, "author-description")]/text()').get()

        yield authors_items(
            name=name,
            born=born,
            description=description
        )