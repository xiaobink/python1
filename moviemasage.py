import requests,openpyxl,csv
from bs4 import BeautifulSoup
from random import randint
num=0
list=['豆瓣排名','电影名字','豆瓣评分','推荐语','详情链接']

'''
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='movies'
sheet['A1']='豆瓣排名'
sheet['B1']='电影名字'
sheet['C1']='豆瓣评分'
sheet['D1']='推荐语'
sheet['F1']='详情链接'
'''
csv_file=open('豆瓣电影top250.csv','w',newline='',encoding='utf_8_sig')
writer=csv.writer(csv_file)
writer.writerow(list)


while True:

    url0='https://movie.douban.com/top250?start='+str(num)+'&filter='
    res=requests.get(url0)
    douban=res.text
    num+=25
    soup=BeautifulSoup(douban,'html.parser')
    massages=soup.find_all(class_='item')

    for massage in massages:
        number=massage.find(class_='pic').text.strip()
        name=massage.find('img')['alt']
        star=massage.find('span',class_="rating_num").text
        quote=massage.find(class_='quote').text.strip()
        urlm=massage.find('a')['href']
        #sheet.append([number,name,star,quote,urlm])

        writer.writerow([number,name,star,quote,urlm])


    if num>250:
        break

csv_file.close()
#wb.save('豆瓣电影top250.xlsx')