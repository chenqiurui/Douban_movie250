# -*- coding: utf-8 -*-

from scrapy import cmdline

# 开始爬取
#cmdline.execute('scrapy crawl douban_spider'.split())
# 存储数据
cmdline.execute('scrapy crawl douban_spider -o douban_movie.csv -t csv'.split())
# 导出数据
#cmdline.execute('sz douban_movie.csv'.split())
