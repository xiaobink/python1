import requests
from bs4 import BeautifulSoup
url0='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
num=1
while True:
    query={
    'ct': 24,
    'qqmusic_ver': 1298,
    'remoteplace': 'txt.yqq.lyric',
    'searchid': '101543833057862190',
    'aggr': 0,
    'catZhida': 1,
    'lossless': 0,
    'sem': 1,
    't': 7,
    'p': str(num),
    'n': 5,
    'w': '周杰伦',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': 0,
    'platform': 'yqq.json',
    'needNewCode': 0
    }

    res=requests.get(url0,params=query)
    songlist=res.json()
    num+=1
    lyrics=songlist['data']['lyric']['list']
    for i in range(5):
        list0=lyrics[i]['content'].strip().split('\\n')
        print(list0)
    print('\n')

    if num>3:
        break



