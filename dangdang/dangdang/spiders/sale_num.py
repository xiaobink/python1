import scrapy
from bs4 import BeautifulSoup
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name='dangdang'
    allowed_domain='bang.dangdang.com'
    start_urls=[]
    for page in range(3):
        url_0='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%s'%str(page+1)
        start_urls.append(url_0)

    def parse(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        book_datas=soup.find('ul',class_='bang_list').find_all('li')
        for books in book_datas:
            item=DangdangItem()
            item['author']=books.find(class_='publisher_info').find('a').text
            item['book_name']=books.find_all('a')[1]['title']
            item['book_price']=books.find(class_='price').text[:9]

            yield item