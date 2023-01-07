y = int(input())
x = list(map(int,input().split()))
for i in range(1,y+1):
    print(sum(x[0:i]),end = ' ')