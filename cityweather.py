import requests,smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
url_dict={
    '罗定附城街道':'http://forecast.weather.com.cn/town/weather1dn/101281402003.shtml',
    '番禺区大学城':'http://forecast.weather.com.cn/town/weather1dn/101280102015.shtml'
}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


url=url_dict['罗定附城街道']
res=requests.get(url,headers=headers)
res.encoding='utf-8'
#print(res.status_code)
soup=BeautifulSoup(res.text,'html.parser')
temp_data=soup.find('div',class_="todayLeft")
space=soup.find(class_="weather_zdsk")
suggest=soup.find('div',class_="lv")

time = temp_data.find(class_='time').text.strip()[:-2]
temp=temp_data.find(class_="temp").text.strip()+temp_data.find(class_="tempUnit").text.strip()
weather=temp_data.find(class_='weather').text.strip()
advice=suggest.find_all('dd')[2].text.strip()

result='%s %s\n%s %s\n穿衣建议：%s'%(time,'罗定附城街道天气预报',temp,weather,advice)
