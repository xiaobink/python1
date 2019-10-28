import requests,smtplib,schedule,time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header


account=input('请输入您的邮箱：')
password=input('请输入您的密码:') #是授权码，不是qq密码，可在邮箱设置中查看
receiver = input('请输入收件人邮箱：')
def weather_spider():
    url0='http://www.weather.com.cn/weather/101280601.shtml'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    res=requests.get(url0,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    place=soup.find('title').text.split(',')[0]
    weather=soup.find(class_='wea').text
    temp=soup.find(class_='tem').text
    return(place,weather,temp)


def sendmail(place,tem,weather):
    global account,password,receiver
    mailhost='smtp.qq.com' #把qq邮箱的服务器地址赋值到变量mailhost上，地址需要是字符串格式
    qqmail=smtplib.SMTP() #实例化一个smtplib模块中的SMTP类的对象
    qqmail.connect(mailhost,25) #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号
    qqmail.login(account, password)

    content=place+tem+weather

    message=MIMEText(content,'plain','utf-8') #实例化一个MIMEText邮件对象，需写入三个参数，分别是正文，文本格式，编码，plain是纯文本格式
    subject='今日天气预报'
    message['Subject']=Header(subject,'utf-8')#实例化一个Header邮件头对象，该对象需要写入主题和编码两个参数

    try:
        qqmail.sendmail(account,receiver,message.as_string())#调用sendmail方法，传入三个参数，分别是发件人邮箱，收件人邮箱，字符串格式正文（用as_string()转化)
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

'''
def job():
    print('干活了')
schedule.every(10).minutes.do(job)               每十分钟执行一次job()函数的任务
schedule.every().hour.do(job)                    每*小时执行一次job函数的任务
schedule.every().day.at("10:30").do(job)         每天10：30执行job函数的任务
schedule.every().monday.do(job)                  每周一执行job函数的任务
schedule.every().wenesday.at("13:15").do(job)    每周三13:15执行任务,注意周全是小写字母，不是大写字母开头

while True:
    schedule.run_pending()
    time.sleep(1)
'''
def job():
    print('开始一次任务')
    place,tem,weather=weather_spider()
    sendmail(place,tem,weather)
    print('任务完成')

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)