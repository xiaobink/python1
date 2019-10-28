'''---知识点：split()---'''
''' 1、通过指定分隔符对字符串进行切片，操作对象是字符串，返回的是一个list
    2、str.split(str='',num=string.count(str)) 两个参数；
    3、str是分隔符，默认为所有的空字符（包括空格，换行，制表符等）
        当使用默认参数作为分隔符时，对于中间为空的项会自动忽略
    4、num 是分割次数，默认为-1，即分割所有。若指定num,则分割成num+1个子字符串
    eg：
        str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
        print str.split( );       # 以空格为分隔符，包含 \n
        print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
        结果如下：
        ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
        ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
    5、对于默认的空字符分隔符，重复出现时，只切一次，但所有的空字符都会删除，不会留下
    eg:
        txt = "Google  Runoob  Taobao\n\nFacebook"
        x = txt.split()
        print(x)
        结果如下：
        ['Google', 'Runoob', 'Taobao', 'Facebook']
        
'''