import time
from selenium import webdriver
from bs4 import BeautifulSoup
num=0
driver=webdriver.Chrome()
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') #获取网页
time.sleep(2) #等待两秒，确保网页加载完成

#not_more=driver.find_element_by_class_name('c_tx_thin')

#
for i in range(10):
    get_more = driver.find_element_by_class_name('js_get_more_hot')
    get_more.click()

time.sleep(2)

'''comments=driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('c_b_normal')
print(len(comments))
for comment in comments:
    sweet=comment.find_element_by_tag_name('p') #找到评论
    num+=1
    print('评论%s：%s\n'%(num,sweet.text))
'''
pagesource=driver.page_source
soup=BeautifulSoup(pagesource,'html.parser')
comments=soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li')
print(len(comments))

for comment in comments:
    sweet=comment.find('p')
    num+=1
    print('评论%s：%s\n'%(num,sweet.text))

driver.close()

