x,y = list(map(int,input().split()))
y = []
for i in range(x):
    y.append(list(map(int,input().split())))
y.sort()
for i in range(x):
    print(*y[i])