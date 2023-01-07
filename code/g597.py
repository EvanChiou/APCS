n,m = map(int,input().split())
l,r,w = [],[],[]
score = [0 for i in range(n)]
for i in range(m):
    l.append(0);r.append(0);w.append(0);
    l[i],r[i],w[i] = map(int,input().split())
    for j in range(l[i]-1,r[i]):
        score[j]+=w[i]
t = list(map(int,input().split()))
t.sort()
total = 0
for i in range(n):
    a = score.index(max(score))
    total+=(score[a]*t[i])
    score[a] = -1
print(total)