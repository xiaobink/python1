import requests
from urllib import parse
from bs4 import BeautifulSoup
while True:

    list_url=[]
    url0='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
    url1='https://www.ygdy8.com'
    name=input('请输入您要查询的电影名字：')
    str_name=parse.quote(name.encode('gbk'))
    url=url0+str_name


    res=requests.get(url)
    print('是否请求成功',res.status_code)
    ygdy=res.text
    soup=BeautifulSoup(ygdy,'html.parser')

    movies=soup.find('div',class_='co_content8').find_all('table')
    for movie in movies:
        movies_url=url1+movie.find('a')['href']
        list_url.append(movies_url)
    if list_url==[]:
        print('很遗憾，您搜索的电影，我们暂时还没有收录呢，抱歉！')
    else:
        num=len(list_url)
        print('一共为您搜索到%s个关于%s的下载链接：'%(num,name))
        print(list_url,'\n')
    next=input('继续搜索请输入y,输入其他则退出:')
    if next!='y':
        break
