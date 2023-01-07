def ff(a,b,c,d):
    if(d == -1):return -1
    if(d*b == a):return d
    elif(d*b != a):
        e = (a-d*b)//c
        if(e*c == a-d*b):return d+e
        else:
            return ff(a,b,c,d-1)
x = int(input())
for i in range(x):
    y = list(map(int,input().split()))
    print(ff(y[0],y[1],y[2],y[0]//y[1]))


