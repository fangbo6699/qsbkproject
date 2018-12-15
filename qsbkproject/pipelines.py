# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter
class QsbkprojectPipeline(object):
    # def __init__(self):
    #     self.fp=open("pachong.json","w",encoding="utf-8")
    #
    # def open_spider(self,spider):
    #      print("start________________")
    # def process_item(self, item, spider):
    #     jsonformat=json.dumps(dict(item),ensure_ascii=False)
    #     self.fp.write(jsonformat+"\n")
    #     return item
    #
    # def close_spider(self, spider):
    #     self.fp.close()
    #     print("end___________________")


    # def __init__(self):
    #     self.fp = open("pachong1.json", "wb")
    #     self.exporter=JsonItemExporter(self.fp,ensure_ascii=False)
    # def open_spider(self, spider):
    #     self.exporter.start_exporting()
    #     print("start________________")
    #
    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.exporter.finish_exporting()
    #     self.fp.close()
    #     print("end___________________")

    def __init__(self):
        self.fp = open("tallxiu.json", "wb")
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False)
    def open_spider(self, spider):
        print("start________________")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("end___________________")