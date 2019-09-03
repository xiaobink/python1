import random
punches=['石头','剪刀','布']
key=True

while key:
    for i in range(1,4):
        print('----现在是第%s回合----',%i)
    com_choice=random.choice(punches)
    user_choice=input('请您出拳\n')

    if user_choice not in punches:
        print('您的输入有误，请重新出拳')
        continue

    elif user_choice!=com_choice:
        if user_choice=='石头':
            if com_choice!='布':
                print('对方出%s,恭喜你赢了!'%com_choice)
            else:
                print('对方出%s，很遗憾你输了!'%com_choice)

        elif user_choice=='剪刀':
            if com_choice!='石头':
                print('对方出%s,恭喜你赢了!'%com_choice)
            else:
                print('对方出%s，很遗憾你输了!'%com_choice)
        else:
            if com_choice!='剪刀':
                print('对方出%s,恭喜你赢了!'%com_choice)
            else:
                print('对方出%s，很遗憾你输了!'%com_choice)
        key=input('是否继续游戏，继续请输入y，输入其他则离开')
        if key!='y':
            key=False
    else:
        print('两人都出%s,再来一次'%(user_choice))
        continue



