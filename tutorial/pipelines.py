# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from PIL import Image

class TutorialPipeline(object):

    def open_spider(self, spider):
        print('----------------------------------spider start working---------------------------------------------------')
        self.file = open('item.jl','w')

    def close_spider(self, spider):
        print('----------------------------------spider stop working---------------------------------------------------')
        self.file.close()    

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        print('----------------------------------spider is working---------------------------------------------------')
        return item

class MysqlPipeline(object):
    def __init__(self, host, database, user, password, port, images_store):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db = None
        self.images_store = images_store

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT'),
            images_store = crawler.settings.get('IMAGES_STORE'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(host = self.host, user = self.user, password = self.password, database = self.database, port = self.port, charset = "utf8")
        # print(self.db)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()
        

    def process_item(self, item, spider):
        data = dict(item)
        data.pop('url')
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table,keys,values)
        im = Image.open(self.images_store + data.get('path'))
        data.update(height = im.height, width = im.width)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit() 
        return item
    
class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        format = self.crawler.settings.get('IMAGES_FORMAT')
        path = '/backend/gallery/'
        file_name = path + url.split('=')[-1] + '.' + format
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
    
    def get_media_requests(self, item, info):
        yield Request(item['url'])