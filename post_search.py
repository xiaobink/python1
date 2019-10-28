import requests,random
from bs4 import BeautifulSoup

post_num=input('请输入快递单号：')
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'csrftoken=X6mwOm24JImENL4gGBa9OyhngYiC00Ad-37N3Tds0n0; sortStatus=0; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1570677186,1570677493,1570679369,1570679851; WWWID=WWWC0A7C79BC7A4A872D1BA583F413134A9; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1570697709',
    'Host': 'www.kuaidi100.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.kuaidi100.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
headers1={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url_post='https://www.kuaidi100.com/all/'
url_posttype='https://www.kuaidi100.com/autonumber/autoComNum'
params={
    'resultv2': '1',
    'text': post_num
}
res_type=requests.get(url_posttype,headers=headers1,params=params)
post_type=res_type.json()
type=post_type['auto'][0]['comCode']

url='https://www.kuaidi100.com/query'
params1={
    'type': type,
    'postid': post_num,
    'temp': random.random(),
    'phone': ''
}
res=requests.get(url,headers=headers,params=params1)
post_data=res.json()
print(post_data)










res_name=requests.get(url_post,headers=headers)
soup=BeautifulSoup(res_name.text,'html.parser')

for i in range(2):
    post_names = soup.find(class_="column-%s column-list" % str(i+1)).find_all('a')
    for i in range(len(post_names)):
        post_name=post_names[i].text.strip()
