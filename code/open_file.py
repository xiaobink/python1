file1=open('/Users/fenbin/Desktop/test/abc.txt','r',encoding='utf-8')  #读取文件打开文件
filecontent=file1.read()
print(filecontent)
file1.close()

file1=open('/Users/fenbin/Desktop/test/abc.txt','w',encoding='utf-8')  #写入文件（不保留原内容）
file1.write('张无忌\n')
file1.write('周芷若\n')
file1.close()


file1=open('/Users/fenbin/Desktop/test/abc.txt','r',encoding='utf-8')  
filecontent=file1.read()
print(filecontent)
file1.close()

file1=open('/Users/fenbin/Desktop/test/abc.txt','a',encoding='utf-8')  #追加文件（保留原内容）
file1.write('赵敏\n')
file1.write('宋青书\n')
file1.close()

file1=open('/Users/fenbin/Desktop/test/abc.txt','r',encoding='utf-8')
filecontent=file1.read()
print(filecontent)
file1.close()
