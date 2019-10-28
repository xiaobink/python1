import requests,schedule,time,openpyxl,smtplib,base64
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender='2541913275@qq.com'
password='arwexfpumjoheacf'
receiver_list=['1877926970@qq.com','2104026952@qq.com'] #

#定义邮件文本部分
def mail_text(send_data,name):
    global message
    subject=name
    content=send_data
    message=MIMEMultipart()   #创建一个带附件的邮件实例
    message['From']='xiaobink'   #添加发件人信息
    #message['To']=receiver   #添加收件人信息
    message['Subject']=Header(subject,'utf-8')  #添加邮件中的主题头
    message.attach(MIMEText(content,'plain','utf-8'))    #添加邮件中的正文部分
    return message

#定义邮件附件部分
def mail_attach(message):
    #二进制读方式打开一个txt文件对象
    with open('热搜top15.txt','rb') as f:
        attach1_data=f.read()

    # 构造附件1，传送当前目录下的 test.txt 文件
    attach1=MIMEText(attach1_data,'plain','utf-8')   #根据获取的txt数据来创建附件中的内容
    attach1['content-Type']='application/octet-stream'   #application/octet-stream表示除开plain文本文件外其他所有情况的默认值，应用程序/八位字节流'
    filename = '热搜top15.txt'
    bs_filename=base64.b64encode(filename.encode('utf-8'))
    attach1.add_header('Content-Disposition','attachment',filename='=?utf-8?b?'+bs_filename.decode('utf-8')+'?=')  #添加附件头
    message.attach(attach1)
    return message

#发送邮件
def sendmail(message):
    try:
        global qqmail
        qq_host = 'smtp.qq.com'
        qqmail = smtplib.SMTP_SSL(qq_host, 465)  # 阿里禁用了25端口，所以替换成465端口并修改协议为ssl才能在阿里云上发送邮件
        qqmail.login(sender,password)
        for receiver in receiver_list:
            qqmail.sendmail(sender,receiver,message.as_string())
        print('发送成功')

    except:
        print('发送失败')
    qqmail.quit()

#创建网址编码字典
webname_list=[]
url_dict={
    '微博': ['https://s.weibo.com/top/summary', 'utf-8'],

    '知乎':['https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true','utf-8'],

    '百度':['http://top.baidu.com/buzz?b=1&fr=topbuzz_b341','gbk']

}
#定义请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

#定义热搜榜网址函数
def hot_url():
    soup_list=[]   #创建网页数据列表

    for url in url_dict:                       #遍历网址字典，取出键（网址）
        res=requests.get(url_dict[url][0],headers=headers)  #请求数据
        #print(res.status_code)
        res.encoding=url_dict[url][1]                    #确定编码格式
        soup=BeautifulSoup(res.text,'html.parser')   #获取网页数据
        soup_list.append(soup)   #向网页列表中添加不同的网页数据
        webname_list.append(url+'热搜榜')
    return soup_list,webname_list

#定义微博爬虫函数
def weibo_crawler(soup):
    global result_weibo
    result_weibo=''
    sheet = wb.create_sheet(webname_list[0])
    sheet.append(['排名', '标题', '热度', '相关链接'])
    rankings=soup.find_all('td',class_='td-01')
    keywords=soup.find_all('td',class_='td-02')
    for i in range(16):
        rank=rankings[i].text
        keyword=keywords[i].find('a').text
        num=keywords[i].text[len(keyword)+1:].strip()+'\n'
        if keywords[i].find('a')['href'][:4] == 'java':
            url='https://s.weibo.com'+keywords[i].find('a')['href_to']+'\n\n'
        else:
            url='https://s.weibo.com'+keywords[i].find('a')['href']+'\n\n'
        result_weibo+='%s %s  %s%s'%(rank,keyword,num,url)
        sheet.append([rank, keyword, num, url])

#定义知乎爬虫函数
def zhihu_crawler():#获取含有排名、标题、链接的网页数据
    global result_zhihu
    sheet = wb.create_sheet(webname_list[1])
    sheet.append(['排名', '标题', '热度', '相关链接'])
    result_zhihu=''
    res=requests.get('https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true',headers=headers)
    json_datas=res.json()
    for i in range(15):
        data=json_datas['data'][i]
        rank=i+1    #定义排名
        keyword=data['target']['title']  #获取标题
        url='https://www.zhihu.com/question/'+data['target']['url'][-9:] +'\n\n' #相关获取链接
        num=data['detail_text']+'\n' #获取热度
        result_zhihu+='%s %s  %s%s'%(rank,keyword,num,url)
        sheet.append([rank,keyword,num,url])

#定义百度爬虫函数
def baidu_crawler(soup):
    global result_baidu
    sheet = wb.create_sheet(webname_list[2])
    sheet.append(['排名', '标题', '热度', '相关链接'])
    result_baidu=''
    rankings=soup.find('table',class_='list-table').find_all('td',class_='first')
    keywords=soup.find('table',class_='list-table').find_all('td',class_='keyword')
    urls=soup.find('table',class_='list-table').find_all('td',class_='tc')
    search_num=soup.find('table',class_='list-table').find_all('td',class_='last')
    for i in range(15):
        rank=rankings[i].text.strip()
        keyword=keywords[i].find('a').text
        num=search_num[i].text.strip()+'\n'
        url=urls[i].find('a')['href']+'\n\n'
        result_baidu+='%s %s  %s%s'%(rank,keyword,num,url)
        sheet.append([rank, keyword, num, url])

#定义天气爬虫函数
def weather_crawler():
    url_dict = {
        '罗定附城街道': 'http://forecast.weather.com.cn/town/weather1dn/101281402003.shtml',
        '番禺区大学城': 'http://forecast.weather.com.cn/town/weather1dn/101280102015.shtml'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    url = url_dict['罗定附城街道']
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    # print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    temp_data = soup.find('div', class_="todayLeft")
    space = soup.find(class_="weather_zdsk")
    suggest = soup.find('div', class_="lv")

    time = temp_data.find(class_='time').text.strip()[:-2]  #获取时间
    temp = temp_data.find(class_="temp").text.strip() + temp_data.find(class_="tempUnit").text.strip() #获取温度
    weather = temp_data.find(class_='weather').text.strip()  #获取天气状况
    advice = suggest.find_all('dd')[2].text.strip()  #获取穿衣建议

    result = '%s %s\n温度：%s\n天气状况：%s\n穿衣建议：%s' % (time, '罗定附城街道天气预报', temp, weather, advice) #整理数据
    return result


def job():
    name='各大网站热搜榜top15'
    global wb
    print('开始热搜榜任务')
    wb=openpyxl.Workbook()
    wb.remove(wb.active)
    soup=hot_url()[0]
    weibo_crawler(soup[0])
    zhihu_crawler()
    baidu_crawler(soup[2])
    wb.save('热搜top15.xlsx')
    final_data = '微博热搜榜top15\n%s\n\n知乎热搜榜top15\n%s\n\n百度热搜榜top15\n%s' % (result_weibo, result_zhihu, result_baidu)
    with open('热搜top15.txt','w') as file:
        writer=file.write(final_data)

    sendmail(mail_attach(mail_text(final_data,name)))
    print('热搜榜任务结束')

def job1():
    name='今日天气预报'
    print('开始天气预报任务')
    sendmail(mail_text(weather_crawler(),name))
    print('天气预报任务结束')

def run():
    schedule.every().day.at('07:00').do(job1)
    schedule.every().day.at('19:42').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
run()
