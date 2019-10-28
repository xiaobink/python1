'''---知识点selenium---'''
import time
from selenium import webdriver  #从selenium库中调用webdriver模块

driver=webdriver.Chrome()  #设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') #打开网页

time.sleep(2) #等待2秒

pagesource=driver.page_source  #获取到渲染完整的网页源代码（str类型数据)


teacher=driver.find_element_by_id('teacher')  #解析网页并提取第一个id为teacher的位置
teacher.send_keys('必须是吴枫啊') #模拟按键输入文字
time.sleep(1)
assistant=driver.find_element_by_name('assistant') #找到请输入你喜欢的助教下面输入框位置
assistant.send_keys('都喜欢') #模拟按键输入文字
time.sleep(1)
teacher.clear()        #清除元素的内容
teacher.send_keys('蜘蛛侠')
time.sleep(1)

button=driver.find_element_by_class_name('sub') #找到提交按钮
button.click() #点击提交按钮
time.sleep(1)

'''
常用提取单个元素的方法：
find_element_by_tag_name('h1') 通过元素的名称选择
find_element_by_class_name('title') 通过元素的class属性选择
find_element_by_id('title') 通过元素的id选择
find_element_by_name('hello') 通过元素的name属性选择
find_element_by_link_text('你好，蜘蛛侠') 通过链接文本获取超链接
find_element_by_partial_link_text('你好') 通过链接的部分文本获取超链接

提取所有元素则在element后面加上s,即把element换成elements,其他不变
'''
labels=driver.find_elements_by_class_name('teacher') #获取的是一个list
for label in labels:
    print(label.text)
    print(label.get_attribute('type'))

driver.close() #关闭浏览器

from selenium.webdriver.chrome.options import Options #从options模块中调用Options这个类

chrome_options=Options()  #实例化Options
chrome_options.add_argument('--headless')  #把Chrome浏览器设置为静默模式
driver=webdriver.Chrome(options=chrome_options) #设置引擎为Chrome，在后台默默运行
