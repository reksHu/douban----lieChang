# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import time
from lieChang.items import LiechangItem
class LiechangesipderSpider(scrapy.Spider):
    name = 'lieChangeSipder'
    allowed_domains = ['movie.douban.com']
    url = "https://movie.douban.com/subject/26322642/comments?start={}&limit=20&sort=new_score&status=P&percent_type="
    # url="https://movie.douban.com/top250"
    start_urls = [url.format(0)]

    def parse(self, response):
        comments_note =  response.xpath("//div[@class='comment']")
        for comment in comments_note:
            items = LiechangItem()
            items['comments']= comment.xpath('./p/text()').extract()[0].strip()
            items['commentTime'] = comment.xpath("./h3/span[@class='comment-info']/span[3]/text()").extract()[0].strip()
            yield items
        offset = 0
        while(offset<=200):
            offset = offset + 20
            nextUrl = self.url.format(offset)
            yield scrapy.Request(nextUrl,callback=self.parse_nextPage)

    def parse_nextPage(self,response):
        comments_note = response.xpath("//div[@class='comment']")
        for comment in comments_note:
            items = LiechangItem()
            items['comments'] = comment.xpath('./p/text()').extract()[0].strip()
            items['commentTime'] = comment.xpath("./h3/span[@class='comment-info']/span[3]/text()").extract()[0].strip()
            yield items
