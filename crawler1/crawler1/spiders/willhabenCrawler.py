import scrapy


class QuotesSpider(scrapy.Spider):
    name = "willhabenCrawler"
    start_urls = [
        'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tische-5751/',
    ]

    def parse(self, response):
        #for quote in response.css('div.header.w-brk'):
        for quote in response.css('title'):
            yield {
                
                'title' : quote.css('title::text').extract_first(), 
                

                
                
            }

        for quote in response.css('article.search-result-entry'):
            yield {
               
                
                #TITLE
                #'title' : quote.css('div.header-w-brk span').extract(),
                
                #price
                #'price' : quote.css('div.info span.info-2-price').extract(),
                'price' : quote.css('div.info').extract(),

                
                #description
                'description' : quote.css('div.description::text').extract_first(),
                
                #adress
                ##'adress' : quote.css('div.address-lg.w-brk-ln-1::text').extract(),
                ##'date' : quote.css('div.bottom-2::text').extract(),

                
                #picture
            }

        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
 