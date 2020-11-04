import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
#    start_urls = ['http://toscrape.com/random']
    start_urls = ['http://toscrape.com']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
#        yield {
#                'author_name': response.css('small.author::text').extract_first(),
#                'text': response.css('span.text::text').extract_first(),
#                'tags': response.css('a.tag::text').extract()
#        }
#        for quote in response.css('div.quote'):
#            item = {
#                'author_name': response.css('small.author::text').extract_first(),
#                'text': response.css('span.text::text').extract_first(),
#                'tags': response.css('a.tag::text').extract()
#            }
#            yield item
        # follow pagination link
        urls = responce.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if (next_page_url):
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse) 

        def parse_details(self, response):
            yield {

                'name': response.css('h3.author-title::text').extract_first(),
                'birth_date': response.css('span.author-born-date::text').extract_first(),
            }
