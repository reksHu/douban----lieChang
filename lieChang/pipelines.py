# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3
class LiechangPipeline(object):
    def __init__(self):
        # self.f = open('douban.json','w',encoding='utf-8')
        self.conn = sqlite3.connect('doubanDB1.db')
        self.c = self.conn.cursor()
        sqlStr="CREATE TABLE douban(Id integer primary key AUTOINCREMENT, comment text,commentTime char(500))"
        # sqlStr=""
        self.c.execute(sqlStr)
        self.conn.commit()
    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False)
        # self.f.write(content)
        sqlStr = "insert into douban(comment,commentTime) values(?,?)"

        self.c.execute(sqlStr,(item['comments'],item['commentTime']))
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
        # self.f.close()
