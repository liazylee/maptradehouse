# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:59:31 2017

@author: zhanglu01
"""



import scrapy
#from scrapy.spiders import CrawlSpider,Rule
#from scrapy.linkextractors import LinkExtractor
import re
from scrapy_splash import SplashRequest


class ZiroomSpider(scrapy.Spider):
    # 必须定义
    name = "ziroomBeijing"
    # 初始urls
    start_urls = [
        "http://www.ziroom.com/z/nl/z2-r1-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r1-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r2-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r3-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r4-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r5-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z2-r6-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r1-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r2-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r3-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r4-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r5-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r6-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z1-r7-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008614.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008626.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008613.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008618.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008617.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008623.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008625.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008611.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008615.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008624.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008616.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008620.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r1-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r2-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r3-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r4-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r5-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r6-d23008629.html?p=1",
        "http://www.ziroom.com/z/nl/z6-r7-d23008629.html?p=1",
    ]    

#    rules = (
#        # 匹配正则表达式,处理下一页,结果加到url列表中
#        Rule(LinkExtractor(allow=(r'.*/z/nl/z[1|2|6]\.html\?p=\d+$'), deny=('login\.html'),), callback='parse_items', follow=True,),
#    )
     
    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
             'spider.pipelines.DuplicatesPipeline': 1,
             'spider.pipelines.SavePipeline': 2,
        },
    }
        
    #CrawlSpider中用来处理start_urls中最初的返回的方法
#    def parse_start_url(self, response):
#        self.parse_items(response)
        
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse_detail_item(self, response):
        house_item = response.meta['house_item']
        try:
            house_item['title'] = response.xpath('/html/body/div[3]/div[2]/div[1]/h2/text()').extract()[0].strip()
        except IndexError:
            house_item['title'] = ''
        house_item['link'] = response.url
        try:
            house_item['price'] = re.sub('\D','',response.xpath('/html/body/div[3]/div[2]/div[1]/p/span[2]/span[1]/text()').extract()[0])
        except IndexError:
            house_item['price'] = ''
        try:
            house_item['area'] = re.findall("面积：[\s\S]*?(\d+(?:\.\d+)?).*㎡.*",response.xpath('/html/body/div[3]/div[2]/ul/li[1]/text()').extract()[0])[0]
        except IndexError:
            house_item['area'] = ''
        try:
            house_item['rooms'] = re.findall(".*户型： (\d+)室.*",response.xpath('/html/body/div[3]/div[2]/ul/li[3]/text()').extract()[0])[0]
        except IndexError:
            house_item['rooms'] = ''
        try:
            house_item['halls'] = re.findall(".*室(\d+)厅.*",response.xpath('/html/body/div[3]/div[2]/ul/li[3]/text()').extract()[0])[0]
        except IndexError:
            house_item['halls'] = ''
        try:
            house_item['lng'] = response.xpath('//*[@id="mapsearchText"]/@data-lng').extract()[0]
        except IndexError:
            house_item['lng'] = ''
        try:
            house_item['lat'] = response.xpath('//*[@id="mapsearchText"]/@data-lat').extract()[0]
        except IndexError:
            house_item['lat'] = ''
        try:
            house_item['direction'] = re.sub('朝向： ','',response.xpath('/html/body/div[3]/div[2]/ul/li[2]/text()').extract()[0])
        except IndexError:
            house_item['direction'] = ''
        try:
            house_item['confGen'] = re.findall(".*?(\d+\.?\d*).*",response.xpath('/html/body/div[3]/div[2]/p/a/span/text()').extract()[0])[0]
        except IndexError:
            house_item['confGen'] = ''
        try:
            house_item['confType'] = re.findall(".*?\d+\.?\d* *(.*)$",response.xpath('/html/body/div[3]/div[2]/p/a/span/text()').extract()[0])[0]
        except IndexError:
            house_item['confType'] = ''
        try:
            house_item['privateBathroom'] = '1' if response.xpath('/html/body/div[3]/div[2]/p/span[@class="toilet"]/text()').extract()[0] else '0'
        except IndexError:
            house_item['privateBathroom'] = '0'
        try:
            house_item['privateBalcony'] = '1' if response.xpath('/html/body/div[3]/div[2]/p/span[@class="balcony"]/text()').extract()[0] else '0'
        except IndexError:
            house_item['privateBalcony'] = '0'
        try:
            house_item['district'] = re.findall(".*?\[(.+?) .*",response.xpath('/html/body/div[3]/div[2]/div[1]/p/span[1]/text()').extract()[0])[0]
        except IndexError:
            house_item['district'] = ''
        return house_item

    def parse(self, response):
#        with open("test.txt",'wb') as f:
#            f.write(response.body)
        for li in response.xpath('//*[@id="houseList"]/li'):
            if "clearfix zry" not in li.xpath('@class').extract():
                from spider.spider.items import HouseItem
                house_item = HouseItem()
                try:
                    house_item['time_unit'] = re.findall(".*\((.+)\).*",li.xpath('div[3]/p[1]/span/text()').extract()[0])[0]
                except IndexError:
                    house_item['time_unit'] = ''
                try:
                    house_item['rentType'] = li.xpath('div[2]/div/p[1]/span[4]/text()').extract()[0]
                except IndexError:
                    house_item['rentType'] = ''
                try:
                    house_item['floorLoc'] = re.findall("^(\d+)/.*",li.xpath('div[2]/div/p[1]/span[2]/text()').extract()[0])[0]
                except IndexError:
                    house_item['floorLoc'] = ''
                try:
                    house_item['floorTotal'] = re.findall(".*/(\d+).*$",li.xpath('div[2]/div/p[1]/span[2]/text()').extract()[0])[0]
                except IndexError:
                    house_item['floorTotal'] = ''
                try:
                    for span in li.xpath('div[2]/p/span[2]/span[@class="subway"]'):
                        if span.xpath('text()').extract()[0].find('暖')==1 or span.xpath('text()').extract()[0].find('空调')==1:
                            house_item['heatingType'] = span.xpath('text()').extract()[0]
                            break
                except IndexError:
                    house_item['heatingType'] = ''
                
                try:
                    house_item['nearestSubWayDist'] = re.findall(".*?(\d+)米.*",li.xpath('div[2]/div/p[2]/span/text()').extract()[0])[0]
                except IndexError:
                    house_item['nearestSubWayDist'] = ''
                try:
                    house_item['confStatus'] = '0' if li.xpath('div[1]/a/img/@src').extract()[0].find('defaultPZZ')>=0 else '1'
                except IndexError:
                    house_item['confStatus'] = ''

                detail_page_link = li.xpath('div[2]/h3/a/@href').extract()[0]
                if detail_page_link:
                    detail_page_link = detail_page_link if detail_page_link.find('www')>=0 else 'http://www.ziroom.com'+detail_page_link
                    detail_page_link = detail_page_link if detail_page_link.find('http')>=0 else 'http:'+detail_page_link
                    request = scrapy.Request(detail_page_link, callback=self.parse_detail_item)
                    request.meta['house_item'] = house_item
                    yield request
        
        #请求下一页数据
        if "next" in response.xpath('//*[@id="page"]/a/@class').extract():
            current_page_link = response.url
            if re.match('.*/z/nl/z[1|2|6]-r\d-.+?\.html\?p=\d+$',current_page_link):
                current_page_p = int(re.findall(".*\?p=(\d+).*",current_page_link)[0]) + 1
                current_page_prefix = re.findall("^(.+\?p=).*",current_page_link)[0]
                next_page_link = current_page_prefix + str(current_page_p)
                yield SplashRequest(next_page_link, self.parse, args={'wait': 0.5})
