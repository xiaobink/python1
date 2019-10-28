from selenium import webdriver
from selenium.webdriver.chrome.options import Options  #静默模式需调用Options类
import time

chrome_options=Options()   #实例化Option对象
chrome_options.add_argument('--headless')   #把Chrome浏览器设置为静默模式（不可视化打开浏览器）
driver=webdriver.Chrome(options=chrome_options)  #设置引擎为Chrome，在后台运行
#driver=webdriver.Chrome()   普通打开模式
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)   #等待两秒，等浏览器打开

login=driver.find_element_by_id('user_login')
passwd=driver.find_element_by_id('user_pass')
submit=driver.find_element_by_id('wp-submit')
login.send_keys('spiderman')
passwd.send_keys('crawler334566')
submit.click()
time.sleep(1)

button3=driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
button3.click()
time.sleep(1)

comment=driver.find_element_by_id('comment')
submit3=driver.find_element_by_id('submit')
comment.send_keys('好多selenium了啊啊')
submit3.click()
time.sleep(1)
driver.close()
print('评论完成')