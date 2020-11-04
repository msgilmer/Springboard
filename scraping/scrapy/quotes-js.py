import scrapy
from scrapy_splash import SplashRequest

class QuotesJSSpider(scrapy.Spider):
    name = 'quotesjs'

    def start_requests(self):
        yield SplashRequest(
            url = 'http://quotes.toscrape.com/js',
            callback = self.parse
        )

    def parse(self, request):
        for q in response.css('div.quote'):
            yield {
                    'text': q.css('span.text::text').extract_first(),
                    'author': q.css('small.author::text').extract_first(),
                    'tags': q.css('div.tags > a.tag::text').extract()
            }
