# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import mysql.connector

class DirtycoinPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            port = '3307',
            user = 'root',
            password = '1111',
            database = 'phong12'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS dirtycoin(
            id int NOT NULL auto_increment, 
            title text,
            price text,
            link text,
            PRIMARY KEY (id)
        )
        """)
    def process_item(self, item, spider):

        #self.cur.execute("select * from dirtycoin where content = %s", (item['text'],))
        #result = self.cur.fetchone()

        
        #if result:
           # spider.logger.warn("Item already in database: %s" % item['text'])


        
        #else:
        self.cur.execute(""" insert into dirtycoin (title, price, link) values (%s,%s,%s)""", (
            item["title"],
            item["price"],
            item["link"]
        ))

        self.conn.commit()
    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()
       
