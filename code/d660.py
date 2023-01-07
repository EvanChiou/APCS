x = int(input())
ct = 0
for i in range(x):
    input()
    ct+=1
    h = 0
    l = 0
    y = list(map(int,input().split()))
    for j in range(1,len(y)):
        if(y[j]>y[j-1]):h+=1
        elif(y[j]<y[j-1]):l+=1
    print('Case ',ct,': ',h,' ',l,sep='')