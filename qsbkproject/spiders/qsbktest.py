# -*- coding: utf-8 -*-
import scrapy
from  scrapy.http.response.html import  HtmlResponse
from qsbkproject.items import QsbkprojectItem
class QsbktestSpider(scrapy.Spider):
    name = 'qsbktest'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url="https://www.qiushibaike.com"
    def parse(self, response):
        print("#"*50)
        print(type(response))
        print("#" * 50)
        duanzidivs=response.xpath("//div[@id='content-left']/div")
        print(type(duanzidivs))
        items = []
        for duanzidiv in duanzidivs:
            author=duanzidiv.xpath(".//h2/text()").get().strip()
            print(author)
            content=duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content="".join(content).strip()
            print(content)
            # item=QsbkprojectItem(author=author,content=content)
            # yield item
            item = QsbkprojectItem(author=author, content=content)
            yield item

        next_url=self.base_url+response .xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url,callback=self.parse)



