import requests
know=0
new=0
step=4
true=0
wrong=0
num=10

range_dic={}
code_dic={}
test_dic={}
answer_dic={}

answer_list=[]
words_list=[]
options_list=[]
know_words=[]
new_words=[]
test_list=[]
true_list=[]
wrong_list=[]
url0='https://www.shanbay.com/api/v1/vocabtest/category/?_=1569034796112'
params={
    '_': 1569040621562
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
res=requests.get(url0,params=params,headers=headers)
shanbay=res.json()
for i in range(10):
    name=shanbay['data'][i][1]
    code=shanbay['data'][i][0]
    range_dic[i]=name
    code_dic[name]=code
print('出题范围','\n\n',range_dic,'\n')
user_num=int(input('请输入相应的数字选择此次出题范围：'))
user_select=range_dic[user_num]
com_code=code_dic[user_select]

url1='https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
params1={
    'category': com_code,
    '_': 1569038296885
}
res_test=requests.get(url1,params=params1,headers=headers)
data=res_test.json()

for i in range(num):
    words = data['data'][i]['content']
    answer = data['data'][i]['pk']
    words_list.append(words)
    answer_list.append(answer)
    for j in range(4):
        meaning=data['data'][i]['definition_choices'][j]

        options_list.append(meaning)

option=[options_list[j:j+step] for j in range(0,len(options_list),step)]
for i in range(len(option)):
    test_dic[words_list[i]]=option[i]
    answer_dic[words_list[i]]=answer_list[i]

print('\n现为您推荐%s个单词，认识请输入1，输入其他则表示不认识:'%num)
for word in words_list:
    print(word)
    user_status=input('是否认识：')
    if user_status=='1':
        know_words.append(word)
        know+=1
    else:
        new_words.append(word)
        new+=1
print('%s个单词您一共认识%s个单词，剩下%s个新单词\n,认识的单词有：\n%s\n不认识的单词有:\n%s'%(num,know,new,know_words,new_words))


for know_word in know_words:
    Tpk = answer_dic[know_word]
    print('现在对您所认识的单词进行测试，看您是否熟练掌握!\n请在所给的选项中选择一项\n%s\nA:%s\nB:%s\nC:%s\nD:%s\n'%(know_word,test_dic[know_word][0]['definition'],test_dic[know_word][1]['definition'],test_dic[know_word][2]['definition'],test_dic[know_word][3]['definition']))
    user_answer=input('请选择')

    if user_answer=='a'or user_answer=='A':
        pk = test_dic[know_word][0]['pk']
        if pk==Tpk:
            true+=1
            true_list.append(know_word)
        else:
            wrong+=1
            wrong_list.append(know_word)
    elif user_answer=='b'or user_answer=='B':
        pk = test_dic[know_word][1]['pk']
        if pk == Tpk:
            true += 1
            true_list.append(know_word)
        else:
            wrong += 1
            wrong_list.append(know_word)
    elif user_answer=='c'or user_answer=='C':
        pk = test_dic[know_word][2]['pk']
        if pk == Tpk:
            true += 1
            true_list.append(know_word)
        else:
            wrong += 1
            wrong_list.append(know_word)
    elif user_answer=='d'or user_answer=='D':
        pk = test_dic[know_word][3]['pk']
        if pk == Tpk:
            true += 1
            true_list.append(know_word)
        else:
            wrong += 1
            wrong_list.append(know_word)
print('\n')
if wrong==0:
    print('此次检测一共%s个单词，其中是您认识%s个单词，剩余%s个生词；\n在认识的%s个单词中做测试时，您答对了%s个单词，答错了%s个单词；\n不认识的单词有：\n%s' % (num,know, new, know, true, wrong, new_words))
else:
    if true==0:
        print('此次检测一共%s个单词，其中是您认识%s个单词，剩余%s个生词；\n在认识的%s个单词中做测试时，您答对了%s个单词，答错了%s个单词；\n答错的单词有:\n%s\n不认识的单词有：\n%s' % (num,know, new, know, true, wrong, wrong_list, new_words))
    else:
        print('此次检测一共%s个单词，其中是您认识%s个单词，剩余%s个生词；\n在认识的%s个单词中做测试时，您答对了%s个单词，答错了%s个单词；\n答错的单词有:\n%s\n不认识的单词有：\n%s'%(num,know,new,know,true,wrong,wrong_list,new_words))












