import calendar

def yearf():
    # 判断是否为闰年，并返回2月的天数
    if calendar.isleap(year):
        two_month=29
    else:
        two_month = 28
    return two_month


def monthf(two_month):
    days = 0
    # 遍历获取输入月份的前几个月份，返回前几个月的总天数
    for every_month in range(month):
        #判断前面的月份是月大还是月小
        if every_month in big_month:
            days += 31

        elif every_month in small_month:
            #判断月小时是否为2月
            if every_month == 2:
                days += two_month
            else:
                days += 30

        else:
            days+=0
    return days

year=int(input('请输入年份：'))
# 分别创建大小月的列表
big_month = [1, 3, 5, 7, 8, 10, 12]
small_month = [2,4, 6, 9, 11]
# 创建变量two_month获取这年2月的天数
two_month=yearf()

# 通过循环判断输入的月份天数是否为正常的
while True:
    month = int(input('请输入月份：'))

    if 0<month<13:
        pass

    # 用户输入月份不在1-12之间，则重新输入
    else:
        print('一年只有12个月噢！')
        continue

    while True:
        day = int(input('请输入几日：'))

        #月大，最多31天，超出则重新输入
        if month in big_month and day>31:
            print('%s月最多有31日'%month)

        # 月小，最多30天（2月最多28或29），超出则重新输入
        elif month in small_month and (day>two_month or day>30):

            if month==2:
                print('这个%s月最多有%s日' % (month,two_month))

            else:
                print('%s月最多有30日' % month)

        #天数不能小于0
        elif day<1:
            print('天数要大于0！')

        # 输入的日期都正常了，则break跳出循环
        else:
            break
    break

#调用monthf()函数，获取前几个月的总天数
days=monthf(two_month)+day
print('%s/%s/%s是%s的第%s天'%(year,month,day,year,days))
