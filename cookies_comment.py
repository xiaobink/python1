import requests,json

session=requests.session()   #实例化一个会话session
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

#获取登入时的cookie，保存到本地
def cookies_get():
    url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data={
        'log': 'spiderman',
        'pwd': 'crawler334566',
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }
    session.post(url,headers=headers,data=data)   #使用post发出登入请求
    cookies=session.cookies
    cookies_dict=requests.utils.dict_from_cookiejar(cookies)  #将服务器给的cookies转化成字典
    print(type(cookies_dict))
    cookies_str=json.dumps(cookies_dict)   #利用json.dumps()将 Python 对象（dict)编码成JSON 字符串（还是字典结构，外层加引号了）
    with open('cookies.txt','w') as file:
        file.write(cookies_str)    #将字符串的cookies保存在本地

#读取本地的cookies文档，并解析成服务器能识别的cookies
def cookies_read():
    with open('cookies.txt','r') as file:
        cookies_str=file.read()
    cookies_dict=json.loads(cookies_str)   #将已编码的 JSON 字符串解码为 Python 对象(dict)
    cookies=requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies

#带着cookies登入，并评论
def comment_in():
    url_comment='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_comment={
        'comment': input('请输入你的评论：'),
        'submit': '发表评论',
        'comment_post_ID': 13,
        'comment_parent': 0
    }
    return (session.post(url_comment,headers=headers,data=data_comment))

#try...except是判断本地是否有cookies文档，有就直接读取登入评论，没有则先登入保存cookies
try:
    session.cookies=cookies_read()
except:
    cookies_get()
    session.cookies=cookies_read()

num=comment_in()
if num.status_code==200:  #判断cookies是否过期
    print('评论成功')
else:
    cookies_get()   #cookies过期需重新获取
    session.cookies=cookies_read()
    comment_in()
    print('已重新登入，并评论')