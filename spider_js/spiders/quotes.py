import scrapy
from scrapy_splash import SplashRequest
from spider_js.items import SpiderJsItem
import unicodedata


class QuoteSpider(scrapy.Spider):

    name = 'quote'
    user_agent = 'Mozilla/5.0'

    def start_requests(self):

        url = 'https://quotes.toscrape.com/js/'

        yield SplashRequest(url=url, headers={'User-Agent': self.user_agent}, callback=self.parse)
        
    def parse(self, response):

        item = SpiderJsItem()
        quotes = response.css('.quote')
        for quote in quotes:

            item['text'] = unicodedata.normalize('NFKD',
                            quote.css('.text::text').get()).encode('ascii', 'ignore').decode("utf-8")
            item['author'] = unicodedata.normalize('NFKD',
                            quote.css('.author::text').get()).encode('ascii', 'ignore').decode("utf-8")
            item['tags'] = quote.css('.tags > a.tag::text').extract()
            
            yield item
        #try to get the next page element
        try:
            next_page = response.css('.next > a').attrib['href']
            next_page = response.urljoin(next_page)
            if next_page is not None:
        
                yield SplashRequest(url=next_page, headers={'User-Agent': self.user_agent}, callback=self.parse)
        except Exception as e:
            print(e)
        

