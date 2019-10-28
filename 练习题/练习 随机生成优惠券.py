import random

# 方法一
# s_list=[]
# coupon_list=[]
#
# # 通过查找找出26个字母的ASCII码十进制数的区间，使用chr将数字转换为26个字母
# #创建列表来存储26个大小写字母
# for i in range(65,91) and range(97,123):
#     s_list.append(chr(i))
#
# #使用choice（）方法来随机选择一个字母，组成优惠券
# for i in range(200):
#     coupon=""
#     for i in range(8):
#         coupon+=random.choice(s_list)
#     coupon_list.append(coupon)
# print(coupon_list)

# 方法二
import string,random
s_list=list(string.ascii_letters)   #ascii_letter生成26个大小写字母，使用list将其分隔开
# s=list(string.ascii_uppercase)    #ascii_uppercase生成26个大写字母的字符串
# s=string.ascii_lowercase          #lowercase生成26个大写字母的字符串

random.shuffle(s_list)       #方法将序列的所有元素随机排序,会改变原列表。
print(''.join(s_list[:8]))  #取乱序后的list中前8个元素连接成字符串

s=string.digits          #digits生成数字0-9的字符串
print(s)