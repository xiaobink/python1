import requests,schedule,smtplib,time,random
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from urllib.parse import quote

url_list=[]
moviename_list=[]


for i in range(3):
    url='https://movie.douban.com/top250?start=%s&filter='%(i*25)
    url_list.append(url)

def moviename_crawler():
    for url in url_list:
        res=requests.get(url)
        soup=BeautifulSoup(res.text,'html.parser')
        #print(res.status_code)
        movie_names=soup.find('ol',class_='grid_view').find_all(class_='info')
        for i,movie_name in enumerate(movie_names):
            name=movie_name.find(class_='title').text.strip()
            moviename_list.append(name)
    return moviename_list

def movies_crawler(moviename_list):
    name_list = []
    num = 0
    last_name = ''
    result=''
    while True:
        for i in range(3):
            name=random.choice(moviename_list)
            name_list.append(name)
        for down_name in name_list:
            gbkmovie=down_name.encode('gbk')
            url_search='http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s'%quote(gbkmovie)
            res=requests.get(url_search)
            res.encoding='gbk'
            soup=BeautifulSoup(res.text,'html.parser')
            url=soup.find(class_='co_content8').find('a')['href']
            if url[1:5]=='html'and down_name is not last_name:
                result+='%s、电影名称：%s\n下载链接：%s\n'%(num+1,down_name,'https://www.ygdy8.com'+url)
                num+=1
                last_name=down_name
            else:
                pass
            if num==3:
                break
        else:
            name_list=[]
        if num == 3:
            break
    return result

def send_email(result):
    sender='2541913275@qq.com'
    password='arwexfpumjoheacf'
    receiver='1877926970@qq.com'
    mailhost='smtp.qq.com'
    qqmail=smtplib.SMTP_SSL(mailhost,465)

    msg=MIMEText(result,'plain','utf-8')
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']='每周电影推荐'

    try:
        print('开始发送')
        qqmail.login(sender,password)
        qqmail.sendmail(sender,receiver,msg.as_string())
        print('发送成功')
    except:
        print('发送失败')
    qqmail.quit()

def job():
    print('开始任务')
    result=movies_crawler(moviename_crawler())
    send_email(result)
    print('任务完成')
schedule.every(5).seconds.do(job)
#schedule.every().friday.at('17:00').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)