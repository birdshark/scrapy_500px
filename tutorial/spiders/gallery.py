# -*- coding: utf-8 -*-
import scrapy
import pymysql
import json
import urllib
import os
from PIL import Image
import time
from tutorial.items import GalleryItem


class GallerySpider(scrapy.Spider):
    name = 'gallery'
    page = 5
    format = 'jpeg'
    def start_requests(self):
        self.format = self.crawler.settings.get('IMAGES_FORMAT')
        urls = []
        for i in range(1,self.page):
            url = 'https://api.500px.com/v1/photos?rpp=50&feature=popular&image_size%5B%5D=36&image_size%5B%5D=2048&sort=&include_states=true&include_licensing=false&formats=' + self.format + '%2Clytro&only=Nature&exclude=&personalized_categories=&rpp=50&page=' + bytes(i)
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        main_data = json.loads(response.body.decode("utf-8"))["photos"]
        for eveData in main_data:
            for image_url in eveData['image_url']:
                name = image_url.split("=").pop() + '.' + self.format
                path = '/backend/gallery/'
                relative_path = path + name
                added_on = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                url = image_url
                gallery = GalleryItem(path = relative_path, size = 0, width = 0, height = 0, added_on = added_on, url = url)
                yield gallery