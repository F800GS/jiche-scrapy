from jiche.items import JicheItem
import scrapy
import re

re_price = r'(?<=class="j-price-td">)\S*'


class JicheSpider(scrapy.Spider):
    name = 'jiche'
    start_urls = ['http://www.jiche.com/pinpai/']

    def parse(self, response):
        for sel in response.xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/div[2]/ul/li/p/a').re(r'http.*(?=\"\>)'):
            #item = JicheItem
            #item['link'] = sel
            url = response.urljoin(sel)
            yield scrapy.Request(url, callback=self.parse_brand)


    def parse_brand(self, response):
        biti = response.xpath('//*[@id="j-model-list"]/li/p/a').re(r'http.*(?=\"\>)')
        for bike in biti:
            urls = response.urljoin(bike)
            yield scrapy.Request(urls, callback=self.parse_last)

    def parse_last(self, response):
        item = JicheItem()
        item['models'] = response.xpath('/html/body/div[2]/div[1]/div/div/div[2]/ul/li[1]/a/text()').extract()
        wlgeca = response.text
        re_price = r'(?<=class="j-price-td">)\S*'
        item['price'] = re.findall(re_price, wlgeca)[0]
        re_payload = r'\d*\sKG'
        item['payload'] = re.findall(re_payload, wlgeca)[0]
        re_capacity = r'\d*\s??cc'
        item['capacity'] = re.findall(re_capacity, wlgeca)[0]
        #print(item['models'],item['capacity'], item['price'], item['payload'])
        return item
    

