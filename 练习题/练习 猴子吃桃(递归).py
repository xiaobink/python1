#逆向递归，把第十天的桃子数量当做是a1
def fn(n):
    if n==1:
        return 1
    else:
        return 2*fn(n-1)+2
print('猴子第一天一共有%s个桃子。'%fn(10))