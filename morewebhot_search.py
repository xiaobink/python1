import requests,openpyxl,smtplib,schedule,time,base64
from bs4 import BeautifulSoup
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #添加附件需要用的对象


sender='2541913275@qq.com'
password='kijffecetiavdiah'
receiver='1877926970@qq.com'

def sendermail(send_data):

    subject='各大网站热搜榜'
    content=send_data
    message = MIMEMultipart()  # 创建一个带附件的实例
    message['From']=sender  #定义邮件头中发件人的信息
    message['To']=receiver      #定义邮件头中收件人的信息
    message['Subject']=Header(subject,'utf-8')         #定义邮件头中的主题
    message.attach(MIMEText(content, 'plain', 'utf-8'))  #添加正文部分到邮件主题中

    #二进制读方式打开一个txt文件对象
    with open('各大网站热搜榜top15.txt','rb') as file:
        attach1_data=file.read()    #获取txt文档中的数据

    # 构造附件1，传送当前目录下的 test.txt 文件
    attach1=MIMEText(attach1_data,'plain','utf-8')    #根据获取的txt数据来创建附件中的内容
    attach1['content-Type']='application/octet-stream'  #application/octet-stream表示除开plain文本文件外其他所有情况的默认值，应用程序/八位字节流'
    filename='各大网站热搜榜top15.txt'
    bs_filename=base64.b64encode(filename.encode('utf-8'))
    attach1.add_header('Content-Disposition','attachment',filename='=?utf-8?b?'+bs_filename.decode('utf-8')+'?=')  #添加附件头
    message.attach(attach1)     #添加附件到邮件主题中


    try:
        mailhost = 'smtp.qq.com'
        qqmail = smtplib.SMTP_SSL(mailhost, 465)   #阿里禁用了25端口，所以替换成465端口并修改协议为ssl才能在阿里云上发送邮件
        qqmail.login(sender, password)
        qqmail.sendmail(sender,receiver,message.as_string())
        print('发送成功！')
    except:
        print('发送失败!')
    qqmail.quit()

#定义请求数据函数
def request_data():
    send_data = ''
    send_datas=''
    final_datas=''  #定义一个空的字符变量用来最终存储全部字符串数据
    need_list = ['微博', '知乎', '微信', '抖音']  # 创建需求网站列表
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url_0='https://tophub.today/'
    res=requests.get(url_0,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    datas=soup.find_all('div',class_='nano-content')
    web_name=soup.find_all('div',class_='cc-cd-lb')

    for data in datas:
        name = web_name[datas.index(data)].text.strip()   #获取网站名字
        if name in need_list:              #是需求的网站，才获取数据
            sheet = wb.create_sheet(name)   #新增一张工作表，并命名
            sheet.append(['排名','标题','热度','相关链接'])  #添加工作表表头
            ranks=data.find_all('span',class_='s')    #获取热搜榜排名网页数据
            titles=data.find_all('span',class_='t')  #获取热搜榜标题网页数据
            search_nums=data.find_all('span',class_='e')  #获取热搜榜热度网页数据
            urls=data.find_all('a')                     #获取热搜榜相关链接网页数据
            del need_list[need_list.index(name)]  # 从列表中删除已匹配的网站名称



            for i in range(15):      #获取每个网站热搜榜的前15名（含15）
                rank=ranks[i].text.strip()   #获取排名
                title=titles[i].text  #获取标题
                num=search_nums[i].text  #获取热度
                url=urls[i]['href']   #获取相关链接
                sheet.append([rank,title,num,url])  #向工作表中添加获取到的数据

                result='%s %s  %s\n相关链接:%s\n\n'%(rank,title,num,url)  #编辑数据格式
                send_data+=result     #存储一个网站的数据

            else:
                send_datas='%s热搜榜Top15：\n'%name+send_data+'\n\n'   #加上热搜所对应的网站名,编辑数据格式
                final_datas+=send_datas    #存储最终数据
                send_data=''      #清空send_data中的数据，为获取下一网站数据做准备


        else:   #不在需求网站名称列表中，则跳过，不获取网页数据
            pass
    return final_datas


def job():
    global wb
    print('开始任务')
    wb=openpyxl.Workbook()   #创建一个Excel表格来存取数据
    wb.remove(wb.active)    #删除默认创建的工作表
    sendermail(request_data())
    request_data()
    wb.save('各大网站热搜榜top15.xlsx')  #保存工作簿
    with open('各大网站热搜榜top15.txt','w',encoding='utf-8') as file:  #创建一个txt文本来存取数据
        file.write(request_data())  #写入数据
        file.close()

    print('任务完成')

schedule.every(5).seconds.do(job)
#schedule.every().day.at('19:00').do(job)  #设定一个定时任务
while True:
    schedule.run_pending()   #开始执行任务
    time.sleep(1)
    

