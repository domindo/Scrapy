
import scrapy

class Dirtycoin(scrapy.Spider):
    name = 'dirtycoin'

    start_urls = ['https://dirtycoins.vn/shop?q=collections:2321137&page=1&view=grid',
                  'https://dirtycoins.vn/shop?q=collections:2321137&page=2&view=grid',
                  'https://dirtycoins.vn/shop?q=collections:2321137&page=3&view=grid',
                  'https://dirtycoins.vn/shop?q=collections:2321137&page=4&view=grid',
                  'https://dirtycoins.vn/shop?q=collections:2321137&page=5&view=grid',
                  'https://dirtycoins.vn/shop?q=collections:2321137&page=6&view=grid',]

    def parse(self, response):
       for products in response.css('div.col-md-3.col-sm-6.col-xs-6'):
            yield {
                    'title' : products.css('a').attrib['title'],
                    'price' : products.css('span.regular-price::text').get().replace('₫','') ,
                    'link'  : products.css('a').attrib['href'] ,
            }