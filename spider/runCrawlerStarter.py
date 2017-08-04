# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:18:34 2017

@author: zhanglu01
"""
import os
os.chdir("/home/li/PycharmProjects/maptradehouse/spider/spider")
from celery import task
from crawlerStarter import crawl_start

@task()
def crawl_run_task():
    return crawl_start()

if __name__ == '__main__':
    crawl_run_task()