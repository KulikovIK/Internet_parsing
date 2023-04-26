import scrapy
from scrapy.http.response.html import HtmlResponse



class QuotesAuthSpider(scrapy.Spider):
    name = "quotes_auth"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response: HtmlResponse):
        csrf_token = response.xpath('//input[@name="csrf_token"]/@value').get()

        yield scrapy.FormRequest.from_response(
            response=response,
            formxpath="//form",
            formdata={
                'csrf_token': csrf_token,
                'username': 'admin',
                'password': 'admin'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        quotes = response.xpath("//div[@class='quote']")
        print(f'Scrapy crawled {len(quotes)} quotes')