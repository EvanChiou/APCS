import math
def jee(a,b):
    if(a>b):x=a;y=b
    else:x=b;y=a
    for i in range(2,y+1):
        if(x%i==y%i==0):return False
    return True
x = 1
while(x!=0):
    y = []
    ct = 0
    ct1 = 0
    x = int(input())
    if(x==0):break
    for i in range(x):
        y.append(int(input()))
    for i in range(len(y)-1):
        for u in range(y.index(y[i])+1,len(y)):
            if(jee(y[i],y[u])):ct+=1
            ct1+=1
    if(ct==0):
        print('No estimate for this data set.')
    else:
        ans = round(math.sqrt(6*(ct1/ct)),6)
        print(ans)


