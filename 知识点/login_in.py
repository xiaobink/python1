'''sessions,cookies:储存在用户本地终端上的数据 #Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份。
    session：会话，可以理解成我们用浏览器上网，到关闭浏览器的这一过程。session是会话过程中，服务器用来记录特定用户会话的信息。
    比如你打开浏览器逛购物网页的整个过程中，浏览了哪些商品，在购物车里放了多少件物品，这些记录都会被服务器保存在session中。
    cookies中存储着session的编码信息，session中存储了cookies的信息，即是说：cookies里带有会话的编码信息，服务器可以立马辨认出该用户，
    同时返回和这个用户特定编码的session（购物车信息）。
    '''
#cookies并不陌生，比如一般当你登录一个网站，你都会在登录页面看到一个可勾选的选项“记住我”，
# 如果你勾选了，以后你再打开这个网站就会自动登录，这就是cookie在起作用。
#当我登入博客账号spiderman，并勾选‘记住我’，服务器就会生成一个cookies和spiderman这个账号绑定，接着把这个cookies告诉浏览器，
#让浏览器保存cookies到本地电脑，当下一次访问博客时，浏览器会带着cookies去访问，服务器会知道你是spiderman，从而不再需要重复输入账号密码。
#cookies是有时效性的，过期后还是要重新登入

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











