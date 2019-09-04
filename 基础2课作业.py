com_num=100
while 1:
    try:
        user_num=int(input('请猜一个整数:'))
    except ValueError:
        print('你输入的不是数字')

    else:
        print('你猜的数字是：%s' % user_num, end=' , ')

        if user_num==com_num:
            print('恭喜你，猜对了')
            break
        elif user_num<com_num:
            print('猜小了')
        else:
            print('猜大了')





