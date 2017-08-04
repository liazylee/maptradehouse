# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:36:53 2017

@author: zhanglu01
"""

from spider.spiders.ziroomSpider import ZiroomSpider

from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CrawlerStartScript():

    def __init__(self):
        self.crawler = CrawlerProcess(get_project_settings())

    def _crawl(self):
        self.crawler.crawl(ZiroomSpider)
        self.crawler.start()
        self.crawler.stop()

    def crawl(self):
        p = Process(target=self._crawl)
        p.start()
        p.join()

crawler = CrawlerStartScript()

def crawl_start():
    crawler.crawl()
