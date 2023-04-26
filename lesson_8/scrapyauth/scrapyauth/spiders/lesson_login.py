import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy_splash import SplashRequest, SplashFormRequest

class LessonLoginSpider(scrapy.Spider):
    name = "lesson_login"
    allowed_domains = ["www.scrapethissite.com"]
    # start_urls = ["http://www.scrapethissite.com/login/"]

    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='http://www.scrapethissite.com/login/',
            endpoint='execute',
            args = {
                'lua_source': self.script
            },
            callback=self.parse
        )

    def parse(self, response: HtmlResponse):
        
        yield scrapy.FormRequest.from_response(
            response=response,
            formxpath="//form",
            formdata={
                'email': 'admin@admin.com',
                'password': 'admin'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        yield SplashRequest(
            url=response,
            endpoint='execute',
            args = {
                'lua_source': self.script
            },
            callback=self.get_text
        )
    
    def get_text(self, response):
        text = response.xpath("//h4[@class='ui-pnotify-title']")
        print(text)
