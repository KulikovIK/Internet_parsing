# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import uuid
from .items import QuotesParserItem, AuthorParserItem

class QuotesParserPipeline:
        
    def open_spider(self, spider):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()
        self.make_quotes_table()
        self.make_author_table()

    def close_spider(self, spider):
        self.connection.close()

    def make_quotes_table(self):
        make_quotes_table = """
        CREATE TABLE IF NOT EXISTS quotes(
            id VARCHAR(36) PRIMARY KEY,
            quote_text TEXT,
            quote_tags TEXT
        )
        """
        self.cursor.execute(make_quotes_table)
        self.connection.commit()

    def make_author_table(self):
        make_author_table = """
        CREATE TABLE IF NOT EXISTS author(
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(25),
            born VARCHAR(25),
            description TEXT
        )
        """
        self.cursor.execute(make_author_table)
        self.connection.commit()

    def insert_quote(self, data):

        insert_db_quote = """
            INSERT INTO quotes VALUES(
                ?, ?, ?
            )
        """

        values = (
            str(uuid.uuid1()),
            str(data.get('text')),
            str(data.get('tags'))
            )
    
        self.cursor.execute(insert_db_quote, values)
        self.connection.commit()

    def insert_author(self, data):
        insert_db_quote = """
            INSERT INTO author VALUES(
                ?, ?, ?, ?
            )
        """

        values = (
            str(uuid.uuid1()),
            str(data.get('name')),
            str(data.get('born')),
            str(data.get('description'))
            )
    
        self.cursor.execute(insert_db_quote, values)
        self.connection.commit()

    def process_item(self, item, spider):

        if isinstance(item, QuotesParserItem):
            self.insert_quote(item)
        if isinstance(item, AuthorParserItem):
            self.insert_author(item)
        return item
