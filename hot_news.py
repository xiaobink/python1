import requests,openpyxl,gevent,csv,selenium,time
from bs4 import BeautifulSoup
from selenium import webdriver  #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options #从options模块中调用Options这个类

chrome_options=Options()  #实例化Options
chrome_options.add_argument('--headless')  #把Chrome浏览器设置为静默模式



url_list=[]
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def get_url():
    url_0='https://news.google.com/?hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans'
    res=requests.get(url_0,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    news=soup.find_all('h3',class_="ipQwMb")
    for new in news[:6]:
        dr = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

        news_url='https://news.google.com/'+new.find('a')['href'][2:]
        url_list.append(news_url)
        dr.get(news_url)
        time.sleep(2)
        # 获取页面title
        title = dr.title
        # 获取页面url
        url = dr.current_url
        print('今日要闻\n%s\n''详情链接:%s' % (title, url))
        #print(new.text)
        #print(news_url)
    return url_list
'''
def news(url_list):
    for url in url_list:
        dr.get(url)
        # 获取页面title
        title = dr.title
        # 获取页面url
        url = dr.current_url
        print('今日要闻\n%s\n''详情链接:%s'%(title,url))

news(get_url())

'''
get_url()


