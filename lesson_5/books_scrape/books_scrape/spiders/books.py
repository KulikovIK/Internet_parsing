import scrapy
from ..items import BooksScrapeItem as items

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.xpath("//ol[@class='row']/li")
        books_link = response.xpath("//ol[@class='row']/li/article/h3/a/@href").getall()
        
        print(f'\n\n{books_link}\n\n')
        
        next_page = response.xpath("//a[contains(text(), 'next')]/@href").get()

        print(f'\n\n{next_page}\n\n')

        if next_page:
            next_page_link = response.urljoin(next_page)
            yield response.follow(url=next_page_link, callback=self.parse)

            
        for book in books_link:

            link = response.urljoin(book)
            yield response.follow(link, callback=self.books_info)

    def books_info(self, response):

        title = response.xpath("//h1/text()").get()
        price = response.xpath("//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]/text()").get()
        in_stock = response.xpath("//div[contains(@class, 'product_main')]/p[contains(@class, 'instock')]/text()").getall()[1].strip()
        product_description = response.xpath("//div[contains(@id, 'product_description')]/following::p[1]/text()").get()
        upc = response.xpath("//table/tr[1]/td/text()").get()
        product_type = response.xpath("//table/tr[2]/td/text()").get()
        price_et = response.xpath("//table/tr[3]/td/text()").get()
        price_it = response.xpath("//table/tr[4]/td/text()").get()
        tax = response.xpath("//table/tr[5]/td/text()").get()
        availability = response.xpath("//table/tr[6]/td/text()").get()
        number_of_reviews = response.xpath("//table/tr[7]/td/text()").get()

        yield items(
            title=title,
            price=price,
            in_stock=in_stock,
            product_description=product_description,
            upc=upc,
            product_type=product_type,
            price_et=price_et,
            price_it=price_it,
            tax=tax,
            availability=availability,
            number_of_reviews=number_of_reviews
            )