import requests,smtplib,base64,os
from bs4 import BeautifulSoup
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid

url_list=[]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

url='http://www.xiachufang.com/explore/'


content=''
mail_msg=''
name_list=[]
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
pictures=soup.find_all('div',class_='cover pure-u')
food_datas=soup.find_all('div',class_='info pure-u')

msg=MIMEMultipart()



for i in range(35):
    as_cid = make_msgid()[1:-1]
    mail_msg+='''
    <p>%s：</p>
    <p><img src="cid:%s"></p>
    <hr>
    <br>
    <br>
    '''%(i+1,as_cid)
    img_name=str(i)+'.jpg'
    with open('./美食图片/'+img_name,'rb') as f:
        img_data = f.read()
    img_msg = MIMEImage(img_data)
    img_msg.add_header('Content-ID','%s'%(as_cid))
    msg.attach(img_msg)
    print(img_name)

msg.attach(MIMEText(mail_msg,'html','utf-8'))


print('下载完成')

qq_host='smtp.qq.com'
qqmail=smtplib.SMTP_SSL(qq_host,465)

sender='1877926970@qq.com'
password='aenoswegaxyfchad'
receiver='2541913275@qq.com'

qqmail.login(sender,password)

msg['From']=sender
msg['To']=receiver
msg['Subject']='本周最受欢迎菜'


qqmail.sendmail(sender,receiver,msg.as_string())
print('发送成功')
qqmail.quit()
