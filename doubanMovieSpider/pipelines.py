# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
class DoubanmoviespiderPipeline(object):
    def __init__(self):
        with open( 'I:\doubanMovieSpider\douBanMovieData.csv', 'a+', encoding='UTF-8' ) as file:
            write = csv.writer(file)
            write.writerow(("排名", "电影名称", "电影评分", "影评人数", "导演", "主演", "剧情", "上映年份", "地区", "标语"))
            file.close()
    def process_item(self, item, spider):
        rank = item['rank']
        name = item['name']
        score = item['score']
        num = item['num']
        qu = item['qu']
        dir = item['dir']
        act = item['act']
        year = item['year']
        type = item['type']
        city = item['city']
        with open('I:\doubanMovieSpider\douBanMovieData.csv','a+',encoding='UTF-8') as doubanDate:
            write = csv.writer(doubanDate)
            write.writerow((rank,name,score,num,dir,act,type,year,city,qu))
            doubanDate.close()
            return item
