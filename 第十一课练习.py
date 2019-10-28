from gevent import monkey #从gevent库中导入monkey模块
monkey.patch_all()    #把程序变成协作式运行，可以帮助程序实现异步
import gevent,time,requests
from gevent.queue import Queue

start=time.time()

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
url_list=[
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/'
] #把8个网站封装成列表

work=Queue() #创建队列对象，并赋值给work,相当于创建了一个不限任何存储数量的空队列。如果我们往Queue()中传入参数，比如Queue(10)，则表示这个队列只能存储10个任务。
for url in url_list:
    work.put_nowait(url)  #用put_nowait()函数把网址都放进队列里

def crawler():  #定义一个crawler（）函数，写明任务具体要做的事情
    while not work.empty():   #当队列不是空的时候，执行下面的程序
        url=work.get_nowait()  #用get_nowait()函数把队列的网址都取出
        res=requests.get(url,headers=headers) #用requests.get()函数爬取网站
        print(url,time.time()-start,work.qsize(),res.status_code) #打印网址，请求时间，work.qsize()队列长度，状态码


task_list=[] #创建空的任务列表

for x in range(8):  #相当于创建了两个爬虫
    task=gevent.spawn(crawler) #用gevent.spawn()函数创建任务,gevent.spawn()的参数是要调用的函数名以及该函数参数
    task_list.append(task)
    print(task_list)
    print(x)


gevent.joinall(task_list) #执行任务列表里的所有任务，就是让爬虫开始爬取网站。

end=time.time() #记录程序结束时间
print(end-start)