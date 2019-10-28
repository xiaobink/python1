from gevent import monkey
monkey.patch_all()
import requests,time,gevent
from gevent.queue import Queue
from bs4 import BeautifulSoup

start=time.time()

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

work=Queue()
url_0='http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_0)
for page in range(4):
    url='%sindex-%s.html'%(url_0,page+2)
    work.put_nowait(url)


def soup_crawler():
    global result
    num = 1
    result = ''
    while not work.empty():
        url=work.get_nowait()

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser').find_all(class_='mov_con')
        for movie_data in soup:
            name = movie_data.find('a').text.strip()
            actors = movie_data.find_all('p')
            if len(actors) == 1:
                actor = actors[0].text.strip()
                brief = '%s、%s\n%s\n' % (num, name, actor)
            elif len(actors) == 2:
                if actors[1].text[:2] == '主演':
                    director = actors[0].text.strip()
                    actor = actors[1].text.strip()
                    brief = '%s、%s\n%s   %s\n' % (num, name, director, actor)

                else:
                    actor = actors[0].text.strip()
                    detail = actors[1].text.strip()
                    brief = '%s、%s\n%s\n简介：%s\n' % (num, name, actor, detail)
            elif len(actors) == 3:
                director = actors[0].text.strip()
                actor = actors[1].text.strip()
                detail = actors[2].text.strip()
                brief = '%s、%s\n%s   %s\n简介：%s\n' % (num, name, director, actor, detail)
            num += 1
            result += brief
task_list=[]

for i in range(2):
    task=gevent.spawn(soup_crawler)
    task_list.append(task)
gevent.joinall(task_list)
end=time.time()
print(result,end-start)




