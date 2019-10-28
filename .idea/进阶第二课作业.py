import requests
from bs4 import BeautifulSoup
res=requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
content=res.text  #将请求到的数据以str类型存到content中
soup=BeautifulSoup(content,'html.parser')  #将str数据转化为BeautifulSoup类型数据
#print(type(soup))
contents=soup.find_all(class_='comment-content')
#print(type(contents))
for content1 in contents:
    user=content1.find('p')

    print(user.text,'\n')