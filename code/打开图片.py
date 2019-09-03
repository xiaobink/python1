
with open('/Users/fenbin/Desktop/test/photo1.png','rb') as file1:
    data=file1.read()
    with open('/Users/fenbin/Desktop/test/photo2.jpg','wb') as file2:
        file2.write(data)
        
        
