import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver=webdriver.Chrome()
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
wait = ui.WebDriverWait(driver,10)
driver.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
wait.until(lambda driver: driver.find_element_by_id('fm-login-id'))
pagesource=driver.page_source


account=driver.find_element_by_id('fm-login-id')
password=driver.find_element_by_id('fm-login-password')
account.send_keys('13415662175')
password.send_keys('binzi668831')

button=driver.find_element_by_class_name('fm-submit')