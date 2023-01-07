x = list(map(int,input().split()))
ct = 0
i = 1
while(i!=len(x)-1):
    if(x[i] == x[i-1]):
        x.pop(i)
    else:
        i+=1
for i in range(1,len(x)-1):
    if(x[i]>x[i-1] and x[i]>x[i+1]):
        ct+=1
print(ct)