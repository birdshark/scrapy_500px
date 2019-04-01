### 创建spider
  scrapy genspider gallery example.com
### 安装库
	pip install Image  
	pip install pymysql
  
### 使用方法
`scrapy crawl example`

### 爬取500px的图片

1. 建表

	      CREATE TABLE `gallery` (  
		    `id` int(11) NOT NULL AUTO_INCREMENT,  
		    `path` varchar(128) NOT NULL,  
		    `size` int(11) NOT NULL,  
		    `width` smallint(6) NOT NULL,  
		    `height` smallint(6) NOT NULL,  
		    `added_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  
		    PRIMARY KEY (`id`),  
		    UNIQUE KEY `unq_path` (`path`)  
		  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

2. 修改配置

    校验信息换成自己的  
  
		    ...
		    DEFAULT_REQUEST_HEADERS = {
		      'Cookie': '***',
		      "x-csrf-token": '***'
		    }
		    ...


    图片路径换成自己的  

    		IMAGES_STORE = '***'

    图片格式png，jpeg二选一  

    		IMAGES_FORMAT = '***'
3. HAPPY CODING