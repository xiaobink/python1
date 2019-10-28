# #求最大公约数
# a=int(input('请输入一个整数：'))
# b=int(input('请再输入一个整数：'))

#动态生成变量locals（）或exec（）
# a=input('请输入你要判断的数（数与数之间用空格分开）：')
# time=int(input('请问你要输入多少个整数：'))
# for i in range(time):
#     n=input('请输入第%s个数：' % (i+1))
#     locals()['a' + str(i)]=n
# for i in range(3):
#     exec('a%s=%s'%(i,i))
# print(a0)
def max_num(*num):
#最大公约数无非就在1-min(num)之间，只要把其中的数都拿去除一遍，最后被整除的那个数一定是最大公约数
    for i in reversed(range(1,min(num)+1)):
        if list(filter(lambda x:x%i,num))==[]:
           return i
# n=max_num(a)
# print('最大公约数为：%s'%n)


#求最小公倍数
# a=int(input('请输入一个整数：'))
# b=int(input('请再输入一个整数：'))

# def multi(*a):
# #最大公约数无非就在1-min(a,b)之间，只要把其中的数都拿去除一遍，最后被整除的那个数一定是最大公约数
#     for i in range(1,min(*a)+1):
#         if a%i==0 and b%i==0:
#             n=i
#
#     # 两个自然数的乘积等于这两个自然数的最大公约数和最小公倍数的乘积。
#     for i in a
#     mul=a*b//n
#     return mul
#
# mul=multi()
# print('%s和%s的最小公倍数为：%s'%(str(a),str(b),mul))
#

# #法一：切片
# s='Crossin的编程教室'
# print(s[::-1])
#
# #法二：reverse()
# s='Crossin的编程教室'
# a=list(s)
# a.reverse()
# print(''.join(a))

# while b:
#     a,b=b,a%b
# print(a)
#
# def s(x,y):
#     if y==0:
#         print(x)
#     else:
#         s(y,x%y)
# s(a,b)