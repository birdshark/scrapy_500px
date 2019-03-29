# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
  'Referer': 'https://500px.com/popular/nature',
  'Origin': 'https://500px.com',
  'Cookie': '_ga=GA1.2.1254045325.1526519705; ab.storage.userId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%2211836343%22%2C%22c%22%3A1526519758389%2C%22l%22%3A1526519758389%7D; ab.storage.deviceId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%2241a5d7d0-ae87-bcf1-7520-87ca2c7dccbe%22%2C%22c%22%3A1526519758394%2C%22l%22%3A1526519758394%7D; device_uuid=a7ac9eb8-e429-4f5b-a814-3e1bc3c4ec5c; optimizelyEndUserId=oeu1551253346643r0.2410314782195857; _gid=GA1.2.1569936239.1551253350; _srt=BAhJIhYxMTgzNjM0MzpiNGVHT0E9PQY6BkVU--d594819edd3b8b6e385f029ec8e9fbd48dd42853; remember_user_token=BAhbB1sGaQO3m7RJIiIkMmEkMTAkTXp4ZktkaTE0YUNSSTJyVFRjVWFIdQY6BkVU--f664a077bb4f95bff00736d7211c5201593ddb84; activity_button_tooltip=1; locale=en; device_uuid=0f31fc77-0046-4aec-aab8-53433a6d2bb3; csrf_token=c0rWXCcVVcRKSNrO8lAovyLyz8J6ok2JvRVaCGFho1U%3D; amplitude_id_9d249102d4736c5a98373c4526f77ae3500px.com=eyJkZXZpY2VJZCI6IjBmMzFmYzc3LTAwNDYtNGFlYy1hYWI4LTUzNDMzYTZkMmJiMyIsInVzZXJJZCI6IjExODM2MzQzIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTUxMzQwODE3ODk0LCJsYXN0RXZlbnRUaW1lIjoxNTUxMzQwODMxMTA5LCJldmVudElkIjoxMCwiaWRlbnRpZnlJZCI6MTUsInNlcXVlbmNlTnVtYmVyIjoyNX0=; ab.storage.sessionId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%229da7550a-2682-74f2-c096-397566826166%22%2C%22e%22%3A1551342657405%2C%22c%22%3A1551340857408%2C%22l%22%3A1551340857408%7D; amplitude_id500px.com=eyJkZXZpY2VJZCI6IjA1NGVkMjUyLWRhZGYtNGVlZi04Y2Y0LWM3MTc5NTBiZjhlYiIsInVzZXJJZCI6IjExODM2MzQzIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTUxMzQwODU3NjA0LCJsYXN0RXZlbnRUaW1lIjoxNTUxMzQwODU3NjExLCJldmVudElkIjo0LCJpZGVudGlmeUlkIjo2LCJzZXF1ZW5jZU51bWJlciI6MTB9; _hpx1=BAh7DUkiD3Nlc3Npb25faWQGOgZFVEkiJWZhMzdlNzM4MDVlY2YwZTc4ZDM3Yzc2OGIxYjAzNWMyBjsAVEkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjsAVFsHWwZpA7ebtEkiIiQyYSQxMCRNenhmS2RpMTRhQ1JJMnJUVGNVYUh1BjsAVEkiCWhvc3QGOwBGIhJhcGkuNTAwcHguY29tSSIJX3NydAY7AEZJIhYxMTgzNjM0MzpiNGVHT0E9PQY7AFRJIhl1c2Vfb25ib2FyZGluZ19tb2RhbAY7AEZUSSIYc3VwZXJfc2VjcmV0X3BpeDNscwY7AEZGSSIQX2NzcmZfdG9rZW4GOwBGSSIxYzByV1hDY1ZWY1JLU05yTzhsQW92eUx5ejhKNm9rMkp2UlZhQ0dGaG8xVT0GOwBGSSIRcHJldmlvdXNfdXJsBjsARkkiDS9wb3B1bGFyBjsAVA%3D%3D--8262f47c355b4b0dbe653ada2c2b1a5f54915c6d',
  "x-csrf-token": 'A5GAYyCoQnQ2XSwFrbIluBU0rRzeJrho7Ww9Afux2hZw21Y/B70XsHwV9stf4g0HN8Zi3qSE9eFQeWcJmtB5Qw=='
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Images stored path
IMAGES_STORE = 'D:/lab/phalcon_multimodule_example/public'
# Image Format
IMAGES_FORMAT = 'jpeg'



ITEM_PIPELINES = {
   'tutorial.pipelines.ImagePipeline': 300,
   'tutorial.pipelines.MysqlPipeline': 301,
  #  'tutorial.pipelines.TutorialPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# MYSQL INFO
MYSQL_HOST = '127.0.0.1'
MYSQL_DATABASE = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = 3306