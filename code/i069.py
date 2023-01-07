x = int(input())
y = list(map(int,input().split()))
mx = max(y)-(sum(y)//x)
y[y.index(max(y))]-=mx;y[y.index(min(y))]+=mx
print(*y)