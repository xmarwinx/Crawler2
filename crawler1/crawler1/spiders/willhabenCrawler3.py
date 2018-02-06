import scrapy
import datetime
from crawler1.items import Crawler1Item
from lxml.html._diffcommand import description



class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawler3"
    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]

    def parse(self, response):
        title = response.css('title').extract_first()
        yield Crawler1Item (title = title, description = 'test'),#, pubDate=pub, file_urls=[imageURL])


    """
    def parse_page(self, response):
        # loop over all cover link elements that link off to the large
        # cover of the magazine and yield a request to grab the cove
        # data and image
        for href in response.xpath("//a[contains(., 'Large Cover')]"):
            yield scrapy.Request(href.xpath("@href").extract_first(),
                self.parse_covers)
 
        # extract the 'Next' link from the pagination, load it, and
        # parse it
        #next = response.css("div.pages").xpath("a[contains(., 'Next')]")
        #yield scrapy.Request(next.xpath("@href").extract_first(), self.parse_page)
        
        
    def parse_covers(self, response):
        # grab the URL of the cover image
        #img = response.css(".art-cover-photo figure a img").xpath("@src")
        #imageURL = img.extract_first()
 
        # grab the title and publication date of the current issue
        title = response.css('.//div[@class="header w-brk"]/a/span/text()').extract_first()
        #year = response.css(".content-main-aside h1 time a::text").extract_first()
        #month = response.css(".content-main-aside h1 time::text").extract_first()[:-2]
 
        # parse the date
        #date = "{} {}".format(month, year).replace(".", "")
        #d = datetime.datetime.strptime(date, "%b %d %Y")
        #pub = "{}-{}-{}".format(d.year, str(d.month).zfill(2), str(d.day).zfill(2))
 
        # yield the result
        yield Crawler1Item(title=title),#, pubDate=pub, file_urls=[imageURL])
        
        
        
        
        for quote in response.xpath('//article[@class="search-result-entry  "]'):
            yield {
               

                #TITLE
                'title' : quote.xpath('.//div[@class="header w-brk"]/a/span/text()').extract_first(),
                
                #price
                #note: propapy doesnt work cause script
                #'price' : quote.xpath('.//div[@class="info"]').extract(),

                
                #description
                'description' : quote.xpath('.//div[@class="description"]/text()').extract_first(),
                
                #adress
                'adress' : quote.xpath('.//div[@class="address-lg w-brk-ln-1 "]/text()').extract_first(),
                'date' : quote.xpath('.//div[@class="bottom-2"]/text()').extract_first(),

                
                
                #image
                #'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract(),
                'image' : quote.xpath('.//section[@class="image-section"]/a/img/@src').extract_first(),
                }
            

        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
        """