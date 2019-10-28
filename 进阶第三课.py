import requests
from bs4 import BeautifulSoup
n=1
movies_list=[]
for i in range(11):
    url0 = 'https://movie.douban.com/top250?start=' + str((n - 1) * 25) + '&filter='
    n+=1
    res=requests.get(url0)

    douban=res.text
    soup=BeautifulSoup(douban,'html.parser')
    main=soup.find_all('div',class_='item')
    '''
    for movies in main:
        num=int(movies.find('em').text)
        name=movies.find('span',class_='title').text.strip()
        url=movies.find('div',class_='hd').find('a')['href']
        star=float(movies.find('span',class_='rating_num').text.strip())
        quote=movies.find('span',class_='inq').text
        list.append([num,name,url,star,quote])
        print(movies(list))
'''
    names=soup.find_all('div',class_='item')
    stars=soup.find_all('div',class_="star")
    quotes=soup.find_all('p',class_='quote')
    for i in range(len(names)):
        list=[int(names[i].find('em').text),names[i].find('a').find('img')['alt'],names[i].find('a')['href'],float(stars[i].text[2:5]),quotes[i].text[1:-1]]
        movies_list.append(list)
print(movies_list)

'''


'''