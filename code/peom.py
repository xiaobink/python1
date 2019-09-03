with open('/Users/fenbin/Desktop/test/peom.txt','w') as file1:
    file1.write('锦瑟\n[唐] 李商隐\n\n锦瑟无端五十弦，\n一弦一柱思华年。\n庄生晓梦迷蝴蝶，\n望帝春心托杜鹃。\n沧海月明珠有泪，\n蓝田日暖玉生烟。\n此情可待成追忆，\n只是当时已惘然。')

with open('/Users/fenbin/Desktop/test/peom.txt','r') as file2:
    lines=file2.readlines()


line1=[]
test_line=['一弦一柱思华年。\n','只是当时已惘然。']
for line in lines:
    if line in test_line:
        line1.append('________________\n\n')
    else:
        line1.append(line+'\n')

with open( '/Users/fenbin/Desktop/test/peom.txt','w') as new:
    new.writelines(line1)
    
