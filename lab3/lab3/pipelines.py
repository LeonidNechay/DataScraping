# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector

class Lab3Pipeline:
    def process_item(self, item, spider):
        return item
    
# class DepPipeline:
#     def process_item(self, item, spider):
#         try:
            
#         except:
#             raise

class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="scrapy"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        # self.cursor.execute("CREATE DATABASE IF NOT EXISTS scrapy;")
        # self.cursor.execute("USE scrapy;")
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS 
                            items (
                                id INT AUTO_INCREMENT,
                                PRIMARY KEY (id),
                                inst_name VARCHAR(50) NOT NULL,
                                inst_url VARCHAR(500)
        );""")
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if self.is_duplicate(item):
            self.cursor.execute("""
                                    UPDATE items
                                    SET inst_url = %s
                                    WHERE inst_name = %s
                                    """,
                                [item.get("inst_url"), item.get("inst_name")]
                                )
        else:
            self.cursor.execute(
                "INSERT INTO items (inst_name, inst_url) VALUES (%s, %s);",
                [item.get("inst_name"), item.get("inst_url")])

        self.connection.commit()
        return item

    def is_duplicate(self, item):
        self.cursor.execute(
            "SELECT COUNT(id) FROM items WHERE inst_name = %s;",
            [item.get("inst_name")])
        count = self.cursor.fetchone()[0]
        return count > 0