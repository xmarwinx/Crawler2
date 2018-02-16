#Testing just the image

import scrapy
import datetime
from crawler1.items import Crawler1Item, Crawler1_detail_view_Item
from lxml.html._diffcommand import description
import re


def format (title):
    return ("%s" % title.strip())

def format2(astring):
    return re.sub('\s+', ' ', astring.strip())

def formatLink(astring):
    return ("http://www.willhaben.at" + astring)


class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawler3"

    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]


    def parse(self, response):

        for article in response.xpath('//article[@class="search-result-entry  "]'):

            # getting the data from the overview page
            searchResult_item = Crawler1Item()
            #searchResult_item['image_urls'] = article.xpath('.//section[@class="image-section"]/a/img/@src').extract()
            #searchResult_item['description'] = format(article.xpath('.//div[@class="description"]/text()').extract_first())
            searchResult_item['title'] = format(article.xpath('.//div[@class="header w-brk"]/a/span/text()').extract_first())
            #searchResult_item['title_link'] = formatLink(article.xpath('.//div[@class="header w-brk"]/a/@href').extract_first())
            #searchResult_item['address'] = format2(article.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract_first())
            #searchResult_item['date'] = format(article.xpath('.//div[@class="bottom-2"]/text()').extract_first())


            # going to each detail view
            detail_view_url =  article.xpath('.//div[@class="header w-brk"]/a/@href').extract_first()
            print ("detail_view_url:", detail_view_url)

            if detail_view_url is not None:
                yield response.follow(detail_view_url, self.parse_detail_view)


            yield searchResult_item

        """
        # There are way too many results so better dont enable this
        next_page_url = response.xpath('//div[@class="search-paging"]/span[@class="nav-icon"]/a/@href').extract()
  
        next_page = str(next_page_url[1])
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        """

    def parse_detail_view(self, response):
        searchResult_detail_view_item = Crawler1_detail_view_Item()
        searchResult_detail_view_item['detail_description'] = response.xpath('.//div[@class="description"]/p/text()').extract_first(default='Error: No description found')
        searchResult_detail_view_item['name'] = response.xpath('.//div[@class="description"]/p/text()').extract_first()


        yield searchResult_detail_view_item
