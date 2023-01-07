n,m,k = map(int,input().split())
Q = []
for i in range(n):
    Q.append(list(map(int,input().split())))
total = [0 for i in range(k)]
for i in range(k):
    c = list(map(int,input().split()))
    tf = [[0 for i in range(m)] for j in range(m)]
    for j in range(n):
        for u in range(m):
            tf[c[j]][u]+=Q[j][u]
    for j in range(m):
        for u in range(m):
            if(j!=u):
                if(tf[j][u]>1000):
                    total[i]+=1000*3
                    total[i]+=(tf[j][u] - 1000) * 2
                else:
                    total[i]+=tf[j][u]*3
            else:
                total[i]+=tf[j][u]
print(min(total))