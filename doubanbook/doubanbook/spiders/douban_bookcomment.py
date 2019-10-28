import requests,scrapy
from bs4 import BeautifulSoup
from ..items import DoubanbookItem

class DoubanbookSpider(scrapy.Spider):
    name='doubanbook'
    allowed_domain=['book.douban.com']
    start_urls=[]
    for page in range(2):
        url_0='https://book.douban.com/top250?start=%s'%(page*25)
        start_urls.append(url_0)

    def parse(self,response):
        soup = BeautifulSoup(response.text, 'html.parser')
        url_data = soup.find(id='wrapper').find_all(class_="pl2")
        for urls in url_data:
            url = urls.find('a')['href']
            yield scrapy.Request(url,callback=self.parse_doubanbook)

    def parse_doubanbook(self,response):
        soup=BeautifulSoup(response.text, 'html.parser')
        book_name = soup.find(id="wrapper").find('span').text
        comment_id = soup.find(id='comments').find_all(class_='comment-info')
        comments = soup.find(id='comments').find_all(class_="short")

        for i in range(len(comments)):
            item=DoubanbookItem()
            item['book_name']=book_name
            item['id'] = comment_id[i].find('a').text.strip()
            item['comment'] = comments[i].text.strip()

            yield item
