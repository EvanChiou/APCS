x = int(input())
y = list(map(int,input().split()))
ans = list(map(int,input().split()))
a,b = ans.copy(),y.copy()
a.sort();b.sort()
def st(r,t):
    y1 = []
    y2 = []
    y3 = []
    for i in range(x):
        if(i<r):
            y1.append(y[i])
        elif(i>t):
            y3.append(y[i])
        else:
            y2.append(y[i])
    y2.sort()
    return y1+y2+y3
if(ans == y):
    print('yes')
if(a != b):
    print('no')
status = y.copy()
for i in range(x):
    if(y[i] == ans[i]):
        status[i] = True
    else:
        status[i] = False
print(status)
strike = [0,0]
for i in range(x):
    if(i == x-1):
        y = st(strike[1],strike[0]+strike[1])
        strike[0],strike[1] = 0,0
    elif(not status[i]):
        if(strike[0] == 0):
            strike[1] = i
        strike[0]+=1
    elif(status[i]):
        print(strike)
        if(strike[0] !=0):
            y = st(strike[1],strike[0]+strike[1]-1)
            strike[0],strike[1] = 0,0
            print(y)
print(y)
