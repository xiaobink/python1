import requests
from urllib import parse
from bs4 import BeautifulSoup
post_dic={}

res=requests.get('https://m.kuaidi100.com/all/?')
all=res.text
soup=BeautifulSoup(all,'html.parser')
postnames=soup.find(id='comList').find_all('dd')
for postnames1 in postnames[:1]:
    a=postnames1.find_all('a')
    for name in a[:-1]:
        post_dic[name.text]=name['data-code']
'''
url0='https://m.kuaidi100.com/result.jsp'
num=input('请输入快递单号：')
post_name=input('请输入快递名称：')
print(post_dic[post_name])

params={
    'nu':str(num),
    'com':post_dic[post_name]
}
'''
#print(url0+'?nu='+str(num)+'&com='+post_dic[post_name])
res_post=requests.get('https://m.kuaidi100.com/result.jsp?nu=9896056706151&com=youzhengguonei')
res_dic=res.text
soup=BeautifulSoup(res_dic,'html.parser')
masage=soup.find('div',class_='main')
print(masage.text)

