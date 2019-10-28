import requests,csv,openpyxl
from bs4 import BeautifulSoup
page=10
url0='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
bool=False

'''
csv_file=open('知乎张佳玮.csv','w',newline='',encoding='utf_8_sig')
writer=csv.writer(csv_file)
writer.writerow(['标题','链接','摘要'])
'''
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='文章'
sheet['A1']='标题'
sheet['B1']='链接'
sheet['C1']='摘要'

while True:
    params={
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': page,
        'limit': 10,
        'sort_by': 'voteups'
    }
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    res=requests.get(url0,params=params,headers=headers)
    print(res.status_code)
    page+=20
    zhihu=res.json()
    datas= zhihu['data']
    for i in range(10):
        title=zhihu['data'][i]['title']
        urlp=datas[i]['url']
        abstract=datas[i]['excerpt']
        bool=zhihu['paging']['is_end']
        sheet.append([title,urlp,abstract])
        #writer.writerow([title,urlp,abstract])
    if page>30:
        break
#csv_file.close()
wb.save('知乎张佳玮.xlsx')

