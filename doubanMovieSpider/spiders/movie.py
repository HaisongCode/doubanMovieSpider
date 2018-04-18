import scrapy
from doubanMovieSpider.items import DoubanmoviespiderItem
from scrapy.selector import Selector
from urllib.parse import urljoin
import time
from scrapy.http import Request
import csv
class MovieSpider(scrapy.Spider):
    name = 'laotan'
    start_urls = ['https://movie.douban.com/top250']
    def parse(self, response):
        item = DoubanmoviespiderItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="item"]')
        for movie in movies:
            #获取电影排名
            movie_rank = movie.xpath('div[@class="pic"]/em/text()').extract()
           #获取名称
            movie_name = movie.xpath('div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract()
            #获取评分
            movie_score = movie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()
            #评分人数
            movie_num = movie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            #标语
            movie_qu= movie.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            #信息
            movie_info = movie.xpath('div[@class="info"]/div[@class="bd"]/p/text()').extract()
            #获取导演、演员、地区、类型、上映年份
            movie_all_info = [info.split() for info in movie_info]
            '''
            [['导演:',
                '邓肯·琼斯',
                'Duncan',
                'Jones',
                '主演:',
                '山姆·洛克威尔',
                'Sam',
                'Rockwell',
                '/',
                '凯文...'],
               ['2009', '/', '英国', '/', '剧情', '科幻', '悬疑'],
               [],
               []]  
            '''
            #演员和导演信息
            dir_act_info = movie_all_info[0]
            '''
                ['导演:',
               '邓肯·琼斯',
               'Duncan',
               'Jones',
               '主演:',
               '山姆·洛克威尔',
               'Sam',
               'Rockwell',
               '/',
               '凯文...'],
            '''
            #从里面提取导演
            movie_dir = dir_act_info[1]
            '''
                邓肯·琼斯   
            '''
            #获取演员
            movie_act = dir_act_info[4::]
            '''
                ['山姆·洛克威尔', 'Sam', 'Rockwell', '/', '凯文...'],
                
            '''
            #获取上映时间、地区以及类型
            ye_ci_ty = movie_all_info[1]
            '''
             ['2009', '/', '英国', '/', '剧情', '科幻', '悬疑']
            '''
            #获取年份
            movie_year = ye_ci_ty[0]
            #获取地区
            moive_city = ye_ci_ty[2]
            #获取类型
            movie_type = ye_ci_ty[-1]
            item['rank'] = movie_rank
            item['name'] = movie_name
            item['score'] = movie_score
            item['num'] = movie_num
            item['qu'] = movie_qu
            item['dir'] =movie_dir
            item['act'] = movie_act
            item['year'] = movie_year
            item['city'] = moive_city
            item['type'] = movie_type
            yield item
        next_url = selector.xpath('//span[@class="next"]/link/@href').extract()
        time.sleep(3)
        if next_url:
            next_url = next_url[0]
            yield Request(urljoin(response.url,next_url),callback=self.parse)


