x = int(input())
for i in range(x):
    y = list(map(int,input().split()))
    if(y[3]/y[2]==y[2]/y[1]==y[1]/y[0]):
        y.append(y[3]*y[3]//y[2])
    else:
        y.append(y[3]+(y[3]-y[2]))
    y = list(map(str,y))
    print(' '.join(y))