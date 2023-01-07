n,l = map(int,input().split())
tree = list(map(int,input().split()))
tree.insert(0,0)
high = list(map(int,input().split()))
x = []
ct = 0
best = 0
for i in range(n):
    x.append(tree[i+1]-tree[i])
    x.append(tree[i+1])
x.append(l-tree[-1])
while(True):
    bk = False
    for i in range(1,n*2,2):
        if(high[((i+1)//2)-1]<=x[i-1] or high[((i+1)//2)-1]<=x[i+1]):
            ct+=1
            if(high[((i+1)//2)-1]>best):best = high[((i+1)//2)-1]
            n-=1
            x.insert(i,x[i+1]+x[i-1])
            x.pop(i+1);x.pop(i+1);x.pop(i-1)
            high.pop(((i+1)//2)-1)
            bk = True
        if(bk):break
    if(bk):continue
    break
print(ct)
print(best)