#方法一 纯if语句
profit=float(input('请输入本月利润(万）：'))
if profit<=10:
    bonus=profit*0.1
else:
    if profit<20:
        bonus = 10 * 0.1 + (profit - 10) * 0.075
    elif 20<=profit<40:
        bonus=10 * 0.1+10* 0.075+(profit-20)*0.05
    elif 40<=profit<60:
        bonus=10 * 0.1+10* 0.075+20*0.05+(profit-40)*0.03
    elif 60<=profit<100:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20*0.03+(profit - 60) * 0.015
    else:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20*0.03+40*0.015+(profit - 100) * 0.001

print('本月应发放奖金总数为：%.4f万元'%bonus)

#方法二
profit=float(input('请输入本月利润(单位：万）：'))
arr=[100,60,40,20,10,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
bonus=0
for n in arr:
    if profit>n:
        bonus+=(profit-n)*rat[arr.index(n)]
        profit=n
print('本月应发放奖金总数为：%.4f万元'%bonus)

