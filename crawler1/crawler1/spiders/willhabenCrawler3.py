#Testing just the image

import scrapy
import datetime
from crawler1.items import Crawler1Item
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

            searchResult_item = Crawler1Item()
            searchResult_item['image_urls'] = article.xpath('.//section[@class="image-section"]/a/img/@src').extract()
            searchResult_item['description'] = format(article.xpath('.//div[@class="description"]/text()').extract_first())
            searchResult_item['title'] = format(article.xpath('.//div[@class="header w-brk"]/a/span/text()').extract_first())
            searchResult_item['title_link'] = formatLink(article.xpath('.//div[@class="header w-brk"]/a/@href').extract_first())
            searchResult_item['address'] = format2(article.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract_first())
            searchResult_item['date'] = format(article.xpath('.//div[@class="bottom-2"]/text()').extract_first())


            yield searchResult_item
