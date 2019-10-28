import requests,smtplib,base64,os
from bs4 import BeautifulSoup
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

url_list=[]
foodname_list=[]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

for page in range(5):
    if page+1==1:
        url='http://www.xiachufang.com/explore/'

    else:
        url='http://www.xiachufang.com/explore/?page=%s'%(page+1)
    url_list.append(url)

def food_crawler():
    num = 0
    mail_msg = ''
    for url in url_list:
        res=requests.get(url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        pictures=soup.find_all('div',class_='cover pure-u')
        food_datas=soup.find_all('div',class_='info pure-u')


        for i in range(10):
            food_name=food_datas[i].find('a').text.strip()    #获取菜名

            detail_url=url[:25]+food_datas[i].find('a')['href']  #获取菜的做法链接
            material=food_datas[i].find(class_='ing ellipsis').text.strip() #获取推荐菜原料
            url_pic=pictures[i].find('img')['data-src']      #获取推荐菜图片的链接
            res=requests.get(url_pic,headers=headers)   #获取推荐菜图片数据
            if os.path.isdir('美食图片'):       #判断当前程序路径下是否存在’美食图片'这个文件夹，不存在则新建
                pass
            else:
                os.mkdir('美食图片')

            # 使用try...except的原因：在网页中获取下来的菜名标题是带有'/,|'这种斜杠会对打开文件的路径造成影响
            #将推荐菜图片保存到本地的美食图片这个文件夹
            try:
                with open('./美食图片/%s.jpg'%food_name,'wb') as file:
                    file.write(res.content)
                    foodname_list.append(food_name)

            except:
                with open('./美食图片/%s.jpg'%i,'wb') as file:  #对于文件名不符合要求的直接采用数字命名进行写入
                    file.write(res.content)
                    foodname_list.append(i)
                    print(i)


            #html格式的文本，要换行则需通过元素来进行换行，可以在内部使用%s这种占位符，和字符串类似
            mail_msg+='''
            %s、%s
            <p>原料：%s</p>
            <p>做法链接：%s</p>
            <p><img src="cid:image%sp"></p>
            <hr>
            <br>
            <br>
            '''%(num+1,food_name,material,detail_url,num)
            num += 1
    print('下载完成')
    return mail_msg,num



def qq_mail(mail_msg,num):
    global msg
    qq_host='smtp.qq.com'
    qqmail = smtplib.SMTP_SSL(qq_host, 465)
    sender='2541913275@qq.com'
    password='arwexfpumjoheacf'
    receiver='1877926970@qq.com'

    msg = MIMEMultipart()   #创建一个带附件的实例（当传输的内容有多种格式时（有文本，有图片），需使用该方法）
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']='本周最受欢迎菜'

    for i,name in enumerate(foodname_list):

        with open('./美食图片/%s.jpg'%name,'rb') as file:
            img_data = file.read()

        img_msg = MIMEImage(img_data)         #实例化一个MIMEImage对象，并将读取到的图片数据赋给该实例
        img_msg.add_header('Content-ID', 'image%sp'%(i)) #对img_msg的content定义一个ID，以便正文html文本中的图片链接到该图片，需注意的是此id不能以数字开头或结尾，否则邮件中会出现重复一张图的现象
        msg.attach(img_msg)         #将图片实例添加到邮件主体中

    msg.attach(MIMEText(mail_msg,'html','utf-8'))  #将html文本添加到邮件主体中

    try:
        qqmail.login(sender, password)
        print('开始发送')
        qqmail.sendmail(sender,receiver,msg.as_string())
        print('发送成功')
    except:
        print('发送失败')
    qqmail.quit()

data=food_crawler()
qq_mail(data[0],data[1])

