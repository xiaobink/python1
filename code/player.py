import time,random



player_win=0
enemy_win=0


while 1:
    for i in range(1,4):
        player_life = random.randint(100,150) # 生成双方角色，并生成随机属性。
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('  \n{}{}{}'.format('——————现在是第',i,'局——————'))                # 展示双方角色的属性
        print('{}\n{}{}\n{}{}'.format('【玩家】','血量:',player_life,'攻击:',player_attack))
        print('------------------------')
        time.sleep(1)
        print('{}\n{}{}\n{}{}'.format('【敌人】','血量:',enemy_life,'攻击:',enemy_attack))
        print('-----------------------')
        time.sleep(1)



        while 1:
            
            enemy_life = enemy_life - player_attack
            print('{}{}'.format('你发起了攻击，【敌人】的血量剩余',enemy_life))
            
            time.sleep(2)
            if enemy_life<0:
                print('玩家获胜')
                player_win+=1
                print('------------------------')
                break

            player_life = player_life - enemy_attack
            print('{}{}'.format('敌人发起了攻击，【玩家】剩余血量',player_life))
            print('------------------------')
            time.sleep(2)
            if player_life<0:
                print('敌方获胜')
                enemy_win+=1
                print('------------------------')         
                break

        else:
            
            if player_life>0 and enemy_life<0:
                player_win+=1
            elif player_life<0 and enemy_life>0:
                enemy_win+=1
            else:
                player_win+=1
                enemy_win+=1

    else:
        
        if player_win>enemy_win:
            print('最终结果：玩家获胜')

        elif player_win<enemy_win:
            print('最终结果：敌方获胜')

        elif player_win==enemy_win:
            print('最终结果：平手')

        print('------------------------\n')
        again=input('再来一局，请输入y,输入其他键退出\n')
        if again!='y':
            break
        
        
     
