# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import codecs
import json

class DuplicatesPipeline(object):
    def __init__(self):
        self.links = set()
 
    def process_item(self, item, spider):
        if item['link'] in self.links:
            # 跑出DropItem表示丢掉数据
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.links.add(item['link'])
            return item

class SavePipeline(object):
    def __init__(self):
        self.filename = "ziroomBeijing.json"
 
    def process_item(self, item, spider):
        with codecs.open(self.filename, 'a', encoding='utf-8') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(line)