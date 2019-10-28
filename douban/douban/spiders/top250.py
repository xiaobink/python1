import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name='douban'
    allowed_domains=['book.douban.com']
    start_ulrs = []
    for page in range(3):
        url_0='https://book.douban.com/top250?start=%s'%str(page*25)
        start_ulrs.append(url_0)

    def parse(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        book_datas=soup.find_all('tr',class_='item')
        for books in book_datas:
            item=DoubanItem()
            item['title']=books.find_all('a')[1]['title']
            item['publish']=books.find('p',class_='pl').text
            item['star']=books.find('span',class_='rating_nums').text
            print(item['title'])

            yield item

