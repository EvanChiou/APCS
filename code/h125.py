x = list(map(int,input().split(' ')))
y = input().split(' ')
a = 0
while(len(y)!=1):
    for i in range(x[1]):
        if(len(y)!=1):y.pop(a)
        else:break
    a = (a*-1)-1
print(y[0])