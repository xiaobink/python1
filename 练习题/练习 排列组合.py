#调用scipy.special模块中comb,per可以计算排列，组合的具体数值
#调用itertools获取排列，组合的全部情况
from scipy.special import comb,perm
print(perm(3,3)) #排列A3,3
print(comb(4,3)) #组合C4,3
#方法一：调用itertools获取组合的全部情况
from itertools import permutations
#从4个数中选3个数出来组合的全部情况：
lst=list(permutations(['1','2','3','4'],3))
result=''
for n in lst:
    result+=''.join(n)+'  '
print('从1,2,3,4个数中选3个数出来组合一共%s种情况\n具体组合为：%s'%(len(lst),result))
#
#
# #方法二：使用集合set()去重
# lst=['1','2','3','4']
# count=0
# result=''
# for i in lst:
#     for j in lst:
#         for k in lst:
#             if len(set(i+j+k))==3:
#                 result+='%s%s%s  '%(i,j,k)
#                 count+=1
# print('从1,2,3,4个数中选3个数出来组合一共%s种情况。\n具体组合为：%s'%(count,result))

#方法三：先确定第一位数，然后从列表中移除，接着确定第二位数，再从列表中移除...
lst=['1','2','3','4']
count=0
result=''
for i in lst:
    lst1=lst.copy()  #拷贝一份列表，因为remove()方法移除元素是在原列表中修改的
    lst1.remove(i)
    for j in lst1:
        lst2=lst1.copy()
        lst2.remove(j)
        for k in lst2:
            result+='%s%s%s  '%(i,j,k)
            count+=1

print('从1,2,3,4个数中选3个数出来组合一共%s种情况。\n具体组合为：%s'%(count,result))

#方法四：使用if去重
lst=['1','2','3','4']
count=0
result=''
for i in lst:
    for j in lst:
        for k in lst:
            if i!=j and i!=k and j!=k:
                result += '%s%s%s  ' % (i, j, k)
                count+=1
print('从1,2,3,4个数中选3个数出来组合一共%s种情况。\n具体组合为：%s'%(count,result))
