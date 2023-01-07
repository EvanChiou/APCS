def dupe(a):
    xx = []
    for i in a:
        xx.append(i.copy())
    return xx
scan = [[0,-1],[-1,0],[0,1],[1,0]]
r,c,k,m = map(int,input().split())
before = []
for i in range(r):
    before.append(list(map(int,input().split())))
after = dupe(before)
def move(a,b,value):
    aft = []
    times = 0
    kk = value//k
    for i in scan:
        try:
            if(a+i[0]<0 or b+i[1]<0):continue
            if(before[a+i[0]][b+i[1]] !=-1):
                aft.append([a+i[0],b+i[1]])
                times+=1
        except:
            continue
    after[a][b]-=kk*times
    return after,aft,kk
def combine(a,b,value):
    for i in b:
        a[i[0]][i[1]]+=value
    return a
for u in range(m):
    for i in range(r):
        for j in range(c):
            if(before[i][j]!=-1):
                v,b,n = move(i,j,before[i][j])
                after = combine(v,b,n)
    before = dupe(after)
mx,mn = -1,1000000
for i in after:
    while(min(i)==-1):
        i.remove(-1)
    if(max(i)>mx):mx = max(i)
    if(min(i)<mn):mn = min(i)
print(mn)
print(mx)
