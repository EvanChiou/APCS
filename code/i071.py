n,m = map(int,input().split());m-=1
lst = list(map(int,input().split()))
curh = lst[m]
count = 0
for i in range(m,-1,-1):
    if(lst[i]>curh):
        count+=1
        curh = lst[i]
curh = lst[m]
for i in range(m,len(lst)):
    if(lst[i]>curh):
        count+=1
        curh = lst[i]
print(count)