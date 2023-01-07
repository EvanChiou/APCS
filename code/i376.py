x = int(input())
y = []
No = True
for i in range(x):
    y.append(list(map(int,input().split())))
for i in range(x):
    mx = max(y[i])
    for u in range(x):
        if(y[i][u] == mx):
            lst = []
            for j in range(x):
                lst.append(y[j][u])
            mn = min(lst)
            if(mx == mn):
                print(i,u)
                No = False
                break
if(No):
    print('No')

