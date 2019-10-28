#定义一个函数，返回1-num之间的质数
def zhishu(num,i=2):
    num_list=[]
    while i<num:
        j=2
        while j<i**0.5:
            if i%j==0:
                break
            j+=1
        else:
            num_list.append(i)
        i+=1
    return num_list

#定义一个函数，判断商num是否为质数，因为短除法中最后一步剩余的商必然是质数
def judge(num,i=2):
    flag=True

    while i<=num**0.5:
        if num%i==0:
            flag=False
            break
        i+=1
    return flag

#判断num是否为合数（分解质因数只针对合数）
while True:

    num=int(input('请输入一个正整数（非质数）：'))
    if num <= 0:
        print('输入不符合要求！')
    else:
        if judge(num):
            if num == 1:
                print('1既不是质数，也不是合数!')
            else:
                print('你输入的是一个质数!')
                print('%s=1*%s'%(num,num))
        else:
            break


#定义s变量存储最终结果
s=str(num)+'='

flag=True
while flag:
    #使用zhishu()函数，实时更新1-num之间的质数list
    num_list=zhishu(num=num)

    #使用for循环遍历质数list，找出短除法式子每一步的最小质数
    for i in num_list:
        if num%i==0:
            #更新短除法后的num以及结果s
            num/=i
            s += str(i) + '*'

            #判断商num是否为质数，是则结束跳出while循环
            if judge(num=num):
                s+=str(int(num))
                flag=False
                break

            #找出最小质数后重新在新的num_list中寻找下一位最小质数
            break

print(s)

