# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanmoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影排名
    rank = scrapy.Field()
    #电影名称
    name = scrapy.Field()
    # #豆瓣评分
    score = scrapy.Field()
    # #影评人数
    num = scrapy.Field()
    # #标语
    qu = scrapy.Field()
    #导演
    dir = scrapy.Field()
    #演员
    act = scrapy.Field()
    #上映年份
    year = scrapy.Field()
    #电影类型
    type = scrapy.Field()
    #电影地区
    city = scrapy.Field()