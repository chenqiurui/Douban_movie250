# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 循环电影条目
        movie_list = response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for item in movie_list:
            # 导入item文件
            douban_item = DoubanItem()
            douban_item['serial_number'] = item.xpath('.//div[@class="item"]//em/text()').extract_first()
            douban_item['movie_name'] = item.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            # 多行数据的处理，把每个电影的分行的介绍信息合并成一个字符串之后，给item
            intro_content = item.xpath('./div/div[2]/div[2]/p[1]/text()').extract()
            content_s = ''
            for intro_string in intro_content:
                content_s += "".join(intro_string.split())
            douban_item['introduce'] = content_s
            douban_item['star'] = item.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            douban_item['comments'] = item.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            douban_item['describe'] = item.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            # 将数据yield到pipeline中，进行数据的清洗和存储
            yield douban_item
        # 处理下一页
        # 先取到url链接，取后一页的链接内容的xpath
        next_link = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)






















