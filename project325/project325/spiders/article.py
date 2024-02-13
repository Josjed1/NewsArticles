import scrapy

from main import link

class ArticleSpider(scrapy.Spider):
    name = "article"

    def parse(self, response):
        pass
