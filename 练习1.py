from gevent import monkey
monkey.patch_all()
import requests,time,gevent,csv,smtplib
from gevent.queue import Queue
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


start=time.time()

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

#定义获取食物详情页链接的爬虫
def url_crawler():
    global work
    work = Queue()   #实例化队列对象
    for group in range(2):
        for page in range(2):
            url='http://www.boohee.com/food/group/%s?page=%s'%(group+1,page+1)
            res=requests.get(url,headers=headers)
            soup=BeautifulSoup(res.text,'html.parser')
            url_sort=soup.find_all(class_='text-box pull-left')

            for i in range(len(url_sort)):
                food_url='http://www.boohee.com'+url_sort[i].find('a')['href']   #获取食物详情页的链接
                work.put_nowait(food_url)   #向队列中添加url
    return work

#定义获取食物某些信息的爬虫
def foodmsg_crawler():
    global food_name,foodmsg_list
    foodmsg_list=[['食物名称','别名','热量','类别','评论']]  #存放向csv文件中添加获取数据
    result = ''
    while not work.empty():
        food_url=work.get_nowait()
        res_food=requests.get(food_url,headers=headers)
        soup_food=BeautifulSoup(res_food.text,'html.parser').find(class_='widget-food-detail pull-left')
        detail = soup_food.find('ul', class_='basic-infor').text.strip()[:-4]  #获取食物的别名，热量，分类
        if detail.split()[0][:2]=='别名':
            other_name=detail.split()[0][3:] #获取食物别名
            num_hot=detail.split()[1][3:]+detail.split()[2]   #获取食物热量
            sort=detail.split()[3][3:]      #获取食物类别
        else:
            other_name = ''     # 获取食物别名
            num_hot = detail.split()[0][3:] + detail.split()[1]  # 获取食物热量
            sort = detail.split()[2][3:]  # 获取食物类别
        pict_url=soup_food.find('img')['src']   #获取食物的图片链接

        comment=soup_food.find('p').text.strip()   #获取评价
        food_name=soup_food.find('img')['alt']    #获取食物名称
        foodmsg_list.append([food_name,other_name,num_hot,sort,comment[3:]])
        res_pict=requests.get(pict_url,headers=headers)
        with open('./食物/'+food_name+'.jpg','wb') as file:
            file.write(res_pict.content)

    print(foodmsg_list)

def send_mail():
    content=''
    sender = '2541913275@qq.com'
    password = 'arwexfpumjoheacf'
    receiver = '1877926970@qq.com'

    mailhost='smtp.qq.com'
    qqmail=smtplib.SMTP_SSL(mailhost,465)

    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']='食物热量详情'

    for i in range(len(foodmsg_list[1:])):
        content+='''
        %s、
        <p><img src="cid:image%sp"</p>
        <p>食物名称：%s</p>
        <p>别名：%s  热量：%s  类别：%s</p>
        <p>%s</p>
        <p></p>
        <br>
        <br>
        <hr>
        '''%(i+1,i,foodmsg_list[1:][i][0],foodmsg_list[1:][i][1],foodmsg_list[1:][i][2],foodmsg_list[1:][i][3],foodmsg_list[1:][i][4])

        with open('./食物/'+foodmsg_list[1:][i][0]+'.jpg','rb') as file:
            image_data=file.read()
        image_msg=MIMEImage(image_data)    #实例化image对象
        image_msg.add_header('Content-ID','image%sp'%i)  #定义image的ID，将图片链接到正文html中的img
        msg.attach(image_msg)

    msg.attach(MIMEText(content, 'html', 'utf-8'))

    try:
        print('开始发送')
        qqmail.login(sender,password)
        qqmail.sendmail(sender,receiver,msg.as_string())
        print('发送成功')
    except:
        print('发送失败')
    qqmail.quit()


url_crawler()
task_list=[]

#创建并添加任务
for i in range(1):
    task=gevent.spawn(foodmsg_crawler)
    task_list.append(task)

gevent.joinall(task_list)  #开启所有任务

#将获取到的信息，以csv格式保存
with open('食物热量.csv', 'w',newline='',encoding='utf-8-sig') as file:
    writer=csv.writer(file)
    for row in foodmsg_list:
        writer.writerow(row)

send_mail()
end=time.time()
print(end-start)

