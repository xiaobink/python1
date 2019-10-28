
count=0
for i in range(1,1000):
    result = 0
    j=1
    while j<i:

        if i%j==0:
            result+=j
        j+=1
    if result==i:
        print(i,end=' ')
        count+=1
print('\n1000以内一共%s个完数，如上'%count)