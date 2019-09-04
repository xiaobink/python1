from random import randint
com_num=randint(0,500)
count=0
while 1:
    try:
        user_num=int(input('请猜一个整数：'))
        count+=1
        print('你输入的数字是：%s'%user_num,end=' , ')
    except ValueError:
        print('你输入的不是数字。')

    else:
        if user_num>com_num:
            print('太大了,再试试。')
        elif user_num<com_num:
            print('太小了，再试试。')
        else:
            print('恭喜你猜对了；\n你一共猜了%s轮。'%count)
            break