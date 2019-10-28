import requests,smtplib,schedule,time
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup

sender=input('请输入发件人邮箱：')
password=input('请输入授权码:')
receiver=input('请输入收件人邮箱:')

def menu_spider():
    num = 0
    url_0='http://www.xiachufang.com/explore/'
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    res=requests.get(url_0,headers=headers)
    res.encoding='utf-8'
    xiachufang=res.text
    soup=BeautifulSoup(xiachufang,'html.parser')
    food_names=soup.find_all(class_='name')
    food_materials=soup.find_all(class_='ellipsis')
    for i in range(len(food_names)):
        name=food_names[i].text.strip()
        url=url_0[:-9]+food_names[i].find('a')['href']
        material=food_materials[i].text.strip()
        num+=1
        return num,name,material,url

def send_mail(num,name,material,url):

    qq_server='smtp.qq.com'
    qqmail=smtplib.SMTP()
    qqmail.connect(qq_server,25)

    qqmail.login(sender,password)

    content='推荐菜%s：%s\n用料：%s\n做法链接：%s\n'%(num,name,material,url)
    subject='本周最受欢迎菜谱'
    message=MIMEText(content,'plain','utf-8')
    message['Subject']=Header(subject,'utf-8')

    try:
        qqmail.sendmail(sender,receiver,message.as_string())
        print('发送成功')
    except:
        print('发送失败')

def job():
    print('开始发送!')
    num,name,material,url=menu_spider()
    send_mail(num,name,material,url)
    print('发送完成')

schedule.every().friday.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)