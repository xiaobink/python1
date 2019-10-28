import requests,openpyxl
from bs4 import BeautifulSoup
from urllib import parse

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='song1'
sheet['A1']='歌曲名'
sheet['B1']='所属专辑'
sheet['C1']='播放时长'
sheet['D1']='播放链接'

while True:
    name = input('请输入你要查询的歌手名字：')
    str_name = parse.quote(name.encode('utf-8'))
    print(str_name)
    for i in range(5):
        url0='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=54465219080617170&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(i+1)+'&n=10&w='+str_name+'&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        res=requests.get(url0)
        music_list=res.json()

        for j in range(10):
            music=music_list['data']['song']['list'][j]
            album=music['album']['name']
            song=music['name']
            time=music['interval']
            url='https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n'
            sheet.append([song,album,time,url])
            print('歌名：%s\n专辑：%s\n播放时长：%s\n歌曲链接：%s'%(song,album,time,url))
        else:
            print('-------------')
    num=input('是否继续搜索，输入y继续，输入其他退出：')
    if num!='y':
        break



wb.save('Jay.xlsx')

