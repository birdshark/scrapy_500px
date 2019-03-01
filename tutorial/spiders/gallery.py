# -*- coding: utf-8 -*-
import scrapy
import pymysql
import json
import urllib
import os
from PIL import Image
import time

class GallerySpider(scrapy.Spider):
    name = 'gallery'
    db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '', db = 'test', charset="utf8")
    cursor = db.cursor()
    def start_requests(self):
        urls = [
            'https://api.500px.com/v1/photos?rpp=50&feature=popular&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36&image_size%5B%5D=2048&sort=&include_states=true&include_licensing=false&formats=jpeg%2Clytro&only=Nature&exclude=&personalized_categories=&page=1&rpp=50',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.body)
        main_data = json.loads(response.body.decode("utf-8"))["photos"]
        for eveData in main_data:
            format = eveData['image_format']
            for image_url in eveData['image_url']:
                name = image_url.split("=").pop() + '.' + format
                web_root = 'D:/lab/phalcon_multimodule_example/public'
                path = '/backend/gallery/'
                full_path = web_root + path + name
                relative_path = path + name
                if os.path.isfile(full_path):
                    print('image has been downloaded')
                else:
                    print('start download image')
                    urllib.urlretrieve(image_url,full_path)
                if os.path.isfile(full_path):
                    print('read image info')
                    im = Image.open(full_path)
                    size = 0
                    width = im.width
                    height = im.height
                    added_on = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                    # print(size)
                    # print(width)
                    # print(height)
                    # print(added_on)
                    sql_insert = "insert into gallery(path, size, width, height, added_on) values ('%s','%d','%d','%d','%s')"
                    data = (relative_path,size,width,height,added_on)
                    print('record it in db')
                    self.cursor.execute(sql_insert % data)
                    self.db.commit()
                else:
                    print('download failed')