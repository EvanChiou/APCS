n,atk = map(int,input().split())
mob= list(map(int,input().split()))
for i in mob:
    if(atk>i):atk+=i
    else:break
print(atk)