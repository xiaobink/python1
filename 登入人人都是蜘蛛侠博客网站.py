import requests,json
session=requests.session()
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

#cookies读取
def cookies_read():
    cookies_txt = open('cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict) #注意是cookiejar_from_dict
    return(cookies)

#账号登入及保存登入时的cookies
def login_in():
    url0 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {
        'log': input('请输入您的账号：'), #spiderman
        'pwd': input('请输入您的密码：'), #crawler334566
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': 1
    }
    session.post(url0,headers=headers,data=data) #在会话下，用post发起登入请求

    #保存cookies
    cookies_dict=requests.utils.dict_from_cookiejar(session.cookies)  #把cookies转化为字典,注意是dict_from_cookiejar
    cookies_str=json.dumps(cookies_dict) #调用json模块中的dumps函数，把cookies从字典转化成字符串

    f=open('cookies.txt','w')
    f.write(cookies_str)
    f.close()

#发表评论
def write_message():
    url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_1={
        'comment': input('请输入你的评论：'),
        'submit': '发表评论',
        'comment_post_ID': 13,
        'comment_parent': 0,
}
    comment=session.post(url_1,headers=headers,data=data_1)
    return(comment.status_code)

try:
    session.cookies=cookies_read()

except FileNotFoundError:
    login_in()
    session.cookies=cookies_read()

num=write_message()
if num==200:
    print('成功啦！')
else:
    login_in()
    session.cookies=cookies_read()
    num =write_message()



