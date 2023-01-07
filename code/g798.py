x = list(map(int,input().split()))
x.pop()
xxx = x.copy()
y = int(input())
for i in range(y):
    if(x[0]>x[1]):
        xxx[1]+=x[0]//10
    for i in range(1,len(x)-1):
        if(x[i]>x[i-1]):
            xxx[i-1]+=x[i]//20
        if(x[i]>x[i+1]):
            xxx[i+1]+=x[i]//20
    if(x[-1]>x[-2]):
        xxx[-2]+=x[-1]//10
    x = xxx.copy()
print(' '.join(list(map(str,x))))