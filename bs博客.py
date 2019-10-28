'''import requests
from bs4 import BeautifulSoup

res=requests.get('http://books.toscrape.com/')
toscrape=res.text
print('请求是否成功',res.status_code)
soup=BeautifulSoup(toscrape,'html.parser')
books_type=soup.find('ul',class_="nav").find('ul').find_all('li')

for book in books_type:
    name=book.find('h')
    print(book.text.strip())
'''



'''import requests
from bs4 import BeautifulSoup
res=requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
tavel=res.text
soup=BeautifulSoup(tavel,'html.parser')
sections=soup.find('ol',class_='row').find_all('li')
#print(type(sections))
for section in sections:
    name=section.find('h3').find('a')
    price=section.find('p',class_="price_color")
    star=section.find('p')
    print('书名：%s\n价格：%s\n星星评分：%s\n'%(name['title'],price.text,star['class'][1]))'''

import requests
from bs4 import BeautifulSoup
res=requests.get('https://spidermen.cn/')
print('请求结果：',res.status_code)
spiders=res.text
soup=BeautifulSoup(spiders,'html.parser')
main=soup.find_all('article')
#print(main)
for book in main:
    name=book.find('h2').find('a')

    time=book.find('time')
    url=book.find('div',class_='entry-meta').find('a')

    print('书名：%s\n发布时间：%s\n链接：%s\n'%(name.text,time['datetime'],url['href']))
