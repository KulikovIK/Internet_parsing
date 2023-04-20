from twisted.internet import reactor

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.books import BooksSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()

    process = CrawlerProcess(settings=settings)
    process.crawl(BooksSpider)

    reactor.run()
