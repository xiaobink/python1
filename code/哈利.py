#读取文件打开文件

file1=open('/Users/fenbin/Desktop/test/scores.txt','r',encoding='utf-8')
file_lines=file1.readlines()

file1.close()

# print(file_lines)

dic={}
list_scores=[]
final_scores=[]
sum_scores=[]

for scores in file_lines:
    # print(score)
    sum=0
    everyone_score=scores.split()
    for i in everyone_score[1:]:
        sum+=int(i)
    else:
        
        sum_score=everyone_score[0]+str(sum)+'\n'
        sum_scores.append(sum_score)

        
file2=open('/Users/fenbin/Desktop/test/sum_score.txt','w',encoding='utf-8')
file2.writelines(sum_scores)
file2.close() 

for i in sum_scores:
    print(i)
    name=i[0:-4]
    score=i[-4:-1]
    # print(name)
    # print(score)
    dic[score]=name
#print(dic)
    list_scores.append(score)
else:
    list_scores.sort(reverse=True)
    for i in list_scores:
        name_score=dic[i]+i+'\n'
        final_scores.append(name_score)
print(final_scores)
with open('/Users/fenbin/Desktop/test/final_scores.txt','w',encoding='utf-8')as file3:
    file3.writelines(final_scores)

        

   


    
    


