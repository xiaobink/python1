import wechat_sender
from wxpy import *

bot=Bot()
my_friend=bot.friends().search('xiaobink')[0]
my_friend.send('hello wechat')
embed()
bot.jion()