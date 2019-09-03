import random,time
punches=['石头','剪刀','布']
key=True

while key:
    user_score=0
    com_score=0
    for i in range(1,4):
        time.sleep(1)
        print('当前比分: user %d-%d computer\n'%(user_score,com_score))
        time.sleep(1.5)
        print('----现在是第%d回合----'%i)
        com_choice=random.choice(punches)
        user_choice=input('请您出拳\n')
        time.sleep(1)

        while user_choice not in punches:
            print('您的出拳有误，请重新出拳')
            user_choice=input()
            time.sleep(1)

        print('\n----战斗过程----')
        print('电脑出了:%s'%com_choice)
        print('你出了：%s'%user_choice)
        time.sleep(1)

        print('----当局结果----')
        if user_choice==com_choice:
            print('平局')
        elif user_choice==punches[punches.index(com_choice)-1]:
            print('你赢了！')
            user_score+=1
            if user_score>1:
                break
        else:
            print('你输了!')
            com_score+=1
            if com_score>1:
                break
    time.sleep(1)
    print('\n最终比分：user %d-%d computer\n最终结果：'%(user_score,com_score),end='')
    if user_score>com_score:
            print('你赢了！')
    elif user_score<com_score:
        print('你输了!')
    else:
        print('平局')
    time.sleep(1)
    key=input('\n是否继续游戏，继续请输入y，输入其他则离开\n')
    if key!='y':
        key=False
            
        
                    


        
    

