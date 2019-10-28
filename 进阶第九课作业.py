import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)

counts=driver.find_elements_by_tag_name('label')
button=driver.find_element_by_id('wp-submit')
user_count=counts[0]
user_count.send_keys('spiderman')
user_pass=counts[1]
user_pass.send_keys('crawler334566')
button.click()

title=driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
title.click()
time.sleep(1)

comment=driver.find_element_by_id('comment')
button1=driver.find_element_by_id('submit')
comment.send_keys('selenium,我来啦！')
button1.click()

driver.close()

