# -*- coding: utf-8 -*-
import scrapy


class StatsSpider(scrapy.Spider):
    name = 'stats'
    allowed_domains = ['stats.nba.com']
    start_urls = ['http://stats.nba.com/']

    def parse(self, response):
        pass
