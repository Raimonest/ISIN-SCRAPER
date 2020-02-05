# -*- coding: utf-8 -*-
import scrapy


class IsinSpiderSpider(scrapy.Spider):
    name = 'isin_spider'
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
    }
    start_urls = ['https://www.isin.ru/ru/ru_isin/news_c/']
    #start_urls = ['https://www.isin.ru/ru/ru_isin/news_c/?id22=643282/']
    def parse(self, response):
        #items=scrapy.items
        all_next_pages = response.xpath('//div').css('.news_sep').xpath('./a/@href').getall()
        all_next_pages.extend(response.xpath('//html/body/table/tr/td/table/tr/td/table/tr/td/a/@href').getall())
        for next_page in all_next_pages:
            if next_page is not None:
                yield response.follow(next_page, self.parse)

        if len(response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[@nowrap]/text()").getall())>0:
            #it has been demonstrated that it gets in here
            try:
                d={}
                for i in range(11):
                    d[response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[i+2]]=response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[i]
                    #self.logger.error(d[response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[i+2]])
                    #self.logger.error(response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[i])
                yield d
                '''yield {
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[2]: ,
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[3]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[1],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[4]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[2],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[5]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[3],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[6]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[4],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[7]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[5],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[8]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[6],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[9]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[7],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[10]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[8],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[11]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[9],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[12]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[10],
                    response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[1]/text()").getall()[13]: response.xpath("//html/body/table/tr/td/table/tr/td/table/tr/td[2]/text()").getall()[11],
                    }'''
            except:
                pass
                
