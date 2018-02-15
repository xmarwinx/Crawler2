#####Crawler Test 1 Just Crawls the Overview page, doesn't got to next page and doens't click links.


import scrapy
import datetime
import re
from crawler1.items import Crawler1Item





def format (title):
    return ("%s" % title.strip())

def format2(astring):
    return re.sub('\s+', ' ', astring.strip())

def formatLink(astring):
    return ("http://www.willhaben.at" + astring)

class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawlerXpath"
    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]




    def parse(self, response):
        

        for quote in response.xpath('//article[@class="search-result-entry  "]'):
            yield {
               
                
                # TITLE
                'title' : format(quote.xpath('.//div[@class="header w-brk"]/a/span/text()').extract_first()),
                'title-link': formatLink(quote.xpath('.//div[@class="header w-brk"]/a/@href').extract_first()),

                # price
                # note: propapy doesnt work cause script
                # 'price' : quote.xpath('.//div[@class="info"]').extract(),

                
                # description
                'description' : format(quote.xpath('.//div[@class="description"]/text()').extract_first()),
                
                # adress
                'address' : format2(quote.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract_first()),
                'date' : format(quote.xpath('.//div[@class="bottom-2"]/text()').extract_first()),
                
                # image
                'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract_first(),
            }


        for article in response.xpath('//article[@class="search-result-entry  "]'):

            previewImage = Crawler1Item()
            previewImage['image_urls'] = article.xpath('.//section[@class="image-section"]/a/img/@src').extract()


            yield previewImage





        #response.xpath('//li[@class=listclass"]/div[not(contains(@class,"divclass"))]/text()').extract()

        # Next button is same as back button need to pick right one...

        next_page_url = response.xpath('//div[@class="search-paging"]/span[@class="nav-icon"]/a/@href').extract_first()
        #next_page_url = response.xpath('//div[@class="search-paging"]/span[@class="nav-icon"]/a[contains(span, text(),"next")]/@href').extract_first()
        # next_page_url_next_or_not = response.xpath('//div[@class="search-paging"]/span[@class="nav-icon"]/a/span').extract_first()

        yield {'URLTOFOLLOW': next_page_url}


        #if "next" in next_page_url_next_or_not:
        #    if next_page_url is not None:
        #        yield response.follow(next_page_url, callback=self.parse)
        #else:
        #    next_page_url = response.xpath(
        #        '//div[@class="search-paging"]/span[@class="nav-icon"]/a/@href').extract_first()
