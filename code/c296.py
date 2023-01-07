a,b,c = list(map(int,input().split()))
p = []
lc = 1
b-=1
for i in range(a):
    p.append(i+1)
for i in range(c):
    lc = (lc+b)%a-1
    p.pop(lc)
    if(lc == -1):lc = 0
    lc+=1
    a-=1
print(p[lc-1])
