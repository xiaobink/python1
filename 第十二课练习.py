from gevent import monkey
monkey.patch_all()    #把程序变成协作运行，实现异步

import requests,csv,time,openpyxl,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue


headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
start=time.time()
num=0

#创建csv文件
csv_file=open('食物热量表.csv','w',newline='',encoding='utf_8_sig')
writer=csv.writer(csv_file)  #实例化一个writer对象
writer.writerow(['序号','食物名称','食物热量','食物营养信息链接']) #调用writer里的writerow()方法

#创建xlsx文件
wb=openpyxl.Workbook()  #创建一个工作簿
sheet=wb.active         #创建一个工作表
sheet.title='食物热量'  #给工作表命名
#创建表头
sheet['A1']='序号'
sheet['B1']='食物名称'
sheet['C1']='食物热量'
sheet['D1']='食物营养信息链接'


work=Queue()  #实例化一个队列对象
#向队列中添加网址
for group in range(11):
    for page in range(3):
        if group==10:
            url_0='http://www.boohee.com/food/view_menu?page=%s'%str(page+1)
            work.put_nowait(url_0)
        else:
            url_0 = 'http://www.boohee.com/food/group/%s?page=%s'%(str(group+1),str(page + 1))
            work.put_nowait(url_0)

#定义爬虫函数，从队列中取出网址
def crawler():
    global num
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        foods_details=soup.find_all(class_='text-box')
        for foods in foods_details:
            food_name=foods.find('a')['title']
            food_calorie=foods.find('p').text
            food_url=url_0[:21]+foods.find('a')['href']
            num+=1
            #按行写入，分别在.csv和.xlsx文件中添加num,food_name,food_calorie,food_url
            writer.writerow([num,food_name,food_calorie,food_url])
            sheet.append([num,food_name,food_calorie,food_url])

task_list=[]  #创建一个空空的任务列表

#向任务列表里添加任务，使用gevent模块
for i in range(5):
    task=gevent.spawn(crawler)  #使用gevent中的spawn()函数创建任务
    task_list.append(task)  #向列表添加任务

#开启所有任务
gevent.joinall(task_list)

csv_file.close()            #关闭打开的csv文件
wb.save('食物热量.xlsx')   #保存为食物热量.xlsx文件
end=time.time()
print(end-start)            #打印出程序运行完所花时间