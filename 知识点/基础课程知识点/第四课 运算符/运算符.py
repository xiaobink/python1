'''---知识点：运算符---'''

#什么是运算符？
##运算符是用于执行程序代码运算，会针对一个以上操作数项目来进行运算

#分类：1.算术运算符 2.赋值运算符 3.比较运算符 4.逻辑运算符 5.条件运算符

#1.算数运算符 表现形式 + - * /
 ## x=1+2  加法运算
 ## x=2-1  减法运算，字符串与字符串之间不可以进行- * /
 ## x='--'*2  乘法运算数，字符串可以与整相乘
print('132'*2) #132132
print('---'*2) #------
 ## x=2/1   除法运算  总是返回的是浮点类型
 ## x=7//3 2 取整运算
 ## x=7%3  1 取余 取模运算
 ## x=2**10 1024 幂运算，可以实现开平方根（**0.5）

 #2.赋值运算符 表现形式 = 将等号右边的值赋值给左边的变量
 ## a=10
 ## += a+=3 相当于 a=a+3
 ## -=
 ## *=
 ## /=
 ## //=
 ## %=


 #3.比较运算符 表现形式 < > <= >= != == is  is not返回布尔值
##字符串比较，对位比较，从左往右，单个字符进行比较，若不能比较出结果，则往后面一位进行比较
r='ab'>'b' #False
print(r)
print('你好'>'你谁')  #False

## == != 比较的是对象的值
## is is not 比较的是对象的id，即判断两个对象是否是同一个对象
print(0==False)  #True  值相等，比较的是值
print(0 is False)  #False id不相等，比较的是id

 #4.逻辑运算符 表现形式 and or not
 ## 0 None 空串list=[],''的bool值是False
 ## and 从左往右找False
 ## or 从左往右找True

 ##非布尔值的与、或运算
#and从左往右找False，找到False,返回相对应的那个值，若没有False，则返回最后一个值
r= 1 and 2  #2
t= 1 and 0  #0
print(r,t)

#or从左往右找True，找到True,返回相对应的那个值，若没有True，则返回最后一个值
r1= 1 or 2  #1
t1= '' or 0 #0
print(r1,t1)


 #5.条件运算符（三元运算符） 表现形式 语句1 if 条件表达式 else 语句2
  ##条件运算符在执行时，会先对条件表达式进行求值判断
  ##如果判断结果为真，则执行语句1，并返回结果，否则执行语句2，再返回结果
print('python') if 1<2 else print('java') #python
a=1
b=2
c=3
m=a if a>b else b
m=m if m>c else c
#m= a if (a>b and a>c) else (b if b>c else c)
print(m)   #3

 #6.运算符的优先级
a=2 or 3 and 4
print(a)  #2
##and 优先级高于or 3and4 返回4（and从左往右找False，没有False ,故返回4）, 2or4 返回2（or从左往右找True，2是True，故返回2）
b=not 4 >2 and 5 <6 or 3<4  #与或非优先级not最高，接着与
print(b) #True