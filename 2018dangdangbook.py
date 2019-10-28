from gevent import monkey
monkey.patch_all()

import requests,openpyxl,gevent,csv
from bs4 import BeautifulSoup
from gevent.queue import Queue

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='2018年当当图书'
sheet['A1']='序号'
sheet['B1']='书名'
sheet['C1']='作者'
sheet['D1']='价钱'

csv_file=open('2018当当图书畅销榜.csv','w',newline='',encoding='utf_8_sig')
writer=csv.writer(csv_file)
writer.writerow(['序号','书名','作者','价钱'])

num=0
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

work=Queue()
for page in range(3):
    url_0='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%s'%str(page+1)
    work.put_nowait(url_0)

def crawler():
    global num
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url_0,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        book_datas=soup.find('ul',class_='bang_list').find_all('li')

        for books in book_datas:

            author=books.find(class_='publisher_info').find('a').text
            book_name=books.find_all('a')[1]['title']
            book_price=books.find(class_='price').text[:9]
            num+=1
            sheet.append([num,book_name,author,book_price])
            writer.writerow([num,book_name,author,book_price])

task_list=[]
for i in range(2):
    task=gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)

wb.save('2018年当当图书畅销榜.xlsx')
csv_file.close()
