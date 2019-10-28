import requests
from bs4 import BeautifulSoup

url0='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=55723257940404706&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
res=requests.get(url0)
print('请求结果:',res.status_code)
musics=res.json()
list_music=musics['data']['song']['list']
for music in list_music:
    print(music['name'])
    print('所属专辑：'+music['album']['name'])
    print('播放时长:'+str(music['interval'])+'秒')
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html')


