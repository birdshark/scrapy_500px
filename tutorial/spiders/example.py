# -*- coding: utf-8 -*-
import scrapy
import pymysql
import time

class ExampleSpider(scrapy.Spider):
    name = "example"
    db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '', db = 'test', charset="utf8")
    cursor = db.cursor()
    def start_requests(self):
        urls = [
            'https://www.fmprc.gov.cn/web/wjbz_673089/zyhd_673091/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pageSize = self.parsePageSize(response)
        for i in range(pageSize):
            if i == 0:
                filename = 'default.shtml'
            else:
                filename = 'default_%d.shtml' % i
            list_url = response.url + filename
            yield scrapy.Request(url=list_url, callback=self.parseList)

    def parseList(self, response):
        articles_url = response.css('div.rebox_news a::attr(href)').extract()
        perfix = "/".join(response.url.split("/")[:-1])
        
        for article_url in articles_url:
            detail_url = perfix + article_url[1:]
            yield scrapy.Request(url=detail_url, callback=self.parseDetail)


    def parseDetail(self, response):
        title = response.css('div.title::text').extract_first()
        st = response.xpath('//span[@id="News_Body_Time"]/text()').extract_first()
        content = response.css('div.content').extract_first()
        timestemp = time.mktime(time.strptime(st, "%Y-%m-%d"))
        sql_insert = "insert into articles(title, created_at, content, updated_at, article_label, article_type, description,article_status) values ('%s','%s','%s','%s','',1,'',1)"
        data = (title,timestemp,content,timestemp)
        self.cursor.execute(sql_insert % data)
        self.db.commit()


    def parsePageSize(self, response):
        pageMatch = response.css("div.page").re(r'var\scountPage\s=\s(\d+)')
        pageSize = int(pageMatch[0])
        return pageSize
