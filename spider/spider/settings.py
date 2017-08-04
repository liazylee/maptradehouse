# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]

#PROXIES = [
#	{'ip_port': '111.207.228.252:8080', 'user_pass': ''},
#	{'ip_port': '117.143.109.165:8080', 'user_pass': ''},
#	{'ip_port': '111.47.219.50:8081', 'user_pass': ''},
#	{'ip_port': '123.206.226.186:8088', 'user_pass': ''},
#	{'ip_port': '210.13.74.154:8080', 'user_pass': ''},
#	{'ip_port': '112.124.23.110:8080', 'user_pass': ''},
#]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'gr_user_id=c4a440d0-2e38-4ca7-aa9f-d8e9c4f50528; PHPSESSID=b4sns0iibjgv23o5iqanpvq371; mapType=%20; CURRENT_CITY_NAME=%E5%8C%97%E4%BA%AC; BJ_nlist=%7B%2260547523%22%3A%7B%22id%22%3A%2260547523%22%2C%22sell_price%22%3A1990%2C%22title%22%3A%22%5Cu901a%5Cu5dde%5Cu7389%5Cu6865%5Cu516b%5Cu901a%5Cu7ebf%5Cu68a8%5Cu56ed%5Cu65b0%5Cu901a%5Cu56fd%5Cu9645%5Cu82b1%5Cu56ed3%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1498898030%2C%22usage_area%22%3A11.5%2C%22floor%22%3A%222%22%2C%22floor_total%22%3A%2214%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F2F%5C%2F48%5C%2FChAFfVlU6TmAJlnlAAyqXzQ3QRY219.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%2C%2260224893%22%3A%7B%22id%22%3A%2260224893%22%2C%22sell_price%22%3A1160%2C%22title%22%3A%22%5Cu987a%5Cu4e49%5Cu987a%5Cu4e49%5Cu57ce15%5Cu53f7%5Cu7ebf%5Cu987a%5Cu4e49%5Cu4ed3%5Cu4e0a%5Cu5c0f%5Cu533a3%5Cu5c45%5Cu5ba4-%5Cu5317%5Cu5367%22%2C%22add_time%22%3A1498898022%2C%22usage_area%22%3A11%2C%22floor%22%3A%225%22%2C%22floor_total%22%3A%226%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F2F%5C%2FC5%5C%2FChAFD1lV7A-AfH0CAAKSAXb-P1s331.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%2C%2260504914%22%3A%7B%22id%22%3A%2260504914%22%2C%22sell_price%22%3A1990%2C%22title%22%3A%22%5Cu987a%5Cu4e49%5Cu987a%5Cu4e49%5Cu57ce15%5Cu53f7%5Cu7ebf%5Cu77f3%5Cu95e8%5Cu897f%5Cu8f9b%5Cu5317%5Cu533a4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1498898010%2C%22usage_area%22%3A19.3%2C%22floor%22%3A%222%22%2C%22floor_total%22%3A%226%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F1D%5C%2F2B%5C%2FChAFD1k2lCCAbkU8AAbkFuv_3nk926.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%7D; gr_session_id_8da2730aaedd7628=d0553554-7ded-4989-89bd-f2b142491615; Hm_lvt_038002b56790c097b74c818a80e3a68e=1498881059,1498897960; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1498898106; _ga=GA1.2.1556007213.1498881060; _gid=GA1.2.675429841.1498881060; _gat=1; CURRENT_CITY_CODE=110000',
    'Host':'www.ziroom.com',
    'Upgrade-Insecure-Requests':'1',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'spider.middlewares.SpiderSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'spider.middlewares.RandomUserAgentMiddleware': 900,
#    'spider.middlewares.RandomProxyMiddleware': 901,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725, 
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://192.168.99.100:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spider.pipelines.SpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# 默认Item并发数：100
CONCURRENT_ITEMS = 100
# 默认Request并发数：16
CONCURRENT_REQUESTS = 16
# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8
# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0




#REDIRECT_ENABLED = False #关掉重定向,不会重定向到新的地址 
#HTTPERROR_ALLOWED_CODES = [504,] #返回504时,按正常返回对待