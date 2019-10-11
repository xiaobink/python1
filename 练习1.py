from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options  #静默模式需调用Options类
import time

chrome_options=Options()   #实例化Option对象
chrome_options.add_argument('--headless')   #把Chrome浏览器设置为静默模式（不可视化打开浏览器）
driver=webdriver.Chrome(options=chrome_options)  #设置引擎为Chrome，在后台运行
#driver=webdriver.Chrome()   普通打开模式
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)   #等待两秒，等浏览器打开

login=driver.find_element_by_id('teacher')
passwd=driver.find_element_by_id('assistant')
submit=driver.find_element_by_class_name('sub')
login.send_keys('吴枫')
passwd.send_keys('艾德')
submit.click()
time.sleep(1)

soup=BeautifulSoup(driver.page_source,'html.parser')
contents=soup.find_all(class_='content')
for i,content in enumerate(contents):
    title=content.text+'\n'
    print(title)

driver.close()
print('评论完成')