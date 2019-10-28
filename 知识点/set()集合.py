'''---知识点：集合set()---'''

'''
    1.集合是无序的，不可重复的，元素写入后是不可改变的，使用{}创建
    2.s={},代表的是一个dict,要创建空set,应写s=set()
    3.set()函数，可以将序列（list，dict，tuple)转化为集合
    
    
'''
s1=set([1,2,3,4])
print(s1)  #{1, 2, 3, 4}

s2=set({'a':1,'b':2}) #当将dict转为set时，转化的是dict的键，没有值
print(s2)  #{'a', 'b'}


s1.add(6)   #使用add向集合添加元素
print(s1)  #{1, 2, 3, 4, 6}


s1.update(s2)  #将一个集合s2中的元素添加到当前集合s1中
print(s1)   #{1, 2, 3, 4, 6, 'a', 'b'}

s1.pop()  #随机删除集合中的一个元素，返回被删除的元素
print(s1)  #{2, 3, 4, 6, 'a', 'b'}

s1.remove(2) #删除集合中的指定元素
print(s1)  #{3, 4, 6, 'b', 'a'}

s1.clear()  #清空集合
print(s1)  #set()

s={1,2,3,4,5}
s1={3,4,5,6,7}
s2={6,7,8}

result=s&s1  #交集运算
print(result)  #{3, 4, 5}

result=s|s1  #并集运算
print(result) #{1, 2, 3, 4, 5, 6, 7}

result=s-s1  #差集运算(就是集合s1中开始出现有交集的前半部分
result1=s-s2
print(result,result1)  #{1, 2} {1, 2, 3, 4, 5}

result=s1^s  #亦或集
print(result)  #

#使用<=检查一个集合是否是另一个集合的子集，结果返回bool值
#使用<检查一个几个是否是另一个集合的真子集
a={1,2,3}
b={1,2,3,4}
result=a<=b #True
result=a<b  #True

#使用>=检查一个集合是否是另一个集合的超集，结果返回bool值
#使用>检查一个几个是否是另一个集合的真超集
#如果一个集合S2中的每一个元素都在集合S1中，且集合S1中可能包含S2中没有的元素，则集合S1就是S2的一个超集，反过来，S2是S1的子集。 S1是S2的超集
a={1,2,3}
b={1,2,3,4,5}
result=b>=a #True
print(result)
result=b>a  #True
print(result)