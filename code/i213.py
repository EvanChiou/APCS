x = int(input())
y = []
for i in range(x):
    a = list(map(int,input().split()))
    if(a[0] == 1):
        y.append(a[1])
    elif(a[0] == 2):
        try:
            print(y[-1])
        except:
            print(-1)
    elif(a[0] == 3):
        try:
            y.pop()
        except:
            pass