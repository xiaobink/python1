import os
if os.path.isfile('热搜top1.txt'):    #判断文件是否存在（存在会返回True）
    print('该文件存在')
else:
    print('不存在')
    if os.path.isdir('不存在的文件夹'): #判断文件夹是否存在
        pass           #存在则跳过
    else:
        os.mkdir('不存在的文件夹')   #不存在则新建这个文件夹
    with open('./不存在的文件夹/132.txt','w') as f:   #在这个文件夹中新建一个文件
        f.write('123')