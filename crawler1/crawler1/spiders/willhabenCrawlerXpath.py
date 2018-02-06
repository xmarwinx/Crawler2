import scrapy
import datetime
import re
#    from crawler1.items import Crawler1Item

def format (title):
    return ("%s" % title.strip())

def format2(astring):
    return re.sub('\s+', ' ', astring.strip())

class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawlerXpath"
    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]



    
    def parse(self, response):
        

        for quote in response.xpath('//article[@class="search-result-entry  "]'):
            yield {
               
                
                #TITLE
                'title' : format(quote.xpath('.//div[@class="header w-brk"]/a/span/text()').extract_first()),
                
                #price
                #note: propapy doesnt work cause script
                #'price' : quote.xpath('.//div[@class="info"]').extract(),

                
                #description
                'description' : format(quote.xpath('.//div[@class="description"]/text()').extract_first()),
                
                #adress
                'adress' : format2(quote.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract_first()),
                'date' : format(quote.xpath('.//div[@class="bottom-2"]/text()').extract_first()),
                
                #image
                'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract_first(),
            }
            



        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
 