n,m,k = map(int,input().split())
K = []
Map = []
count = 0
for i in range(n):
    Map.append([])
    for j in range(m):
        Map[i].append(0)
for i in range(k):
    K.append(list(map(int,input().split())))
while(len(K)!=0):
    for i in K:
        Map[i[0]][i[1]] = -1
    for i in range(len(K)):
        if(K[i][0]+K[i][2]<0 or K[i][0]+K[i][2]>=n):K[i] = None;continue
        if(K[i][1]+K[i][3]<0 or K[i][1]+K[i][3]>=m):K[i] = None;continue
        K[i][0]+=K[i][2]
        K[i][1]+=K[i][3]
    for i in range(K.count(None)):K.remove(None)
    defuse = []
    for i in K:
        if(Map[i[0]][i[1]] == -1):defuse.append([i[0],i[1]]);K[K.index(i)] = None;
    for i in defuse:
        Map[i[0]][i[1]] = 0
    for i in range(K.count(None)):K.remove(None)
for i in Map:
    count+=i.count(-1)
print(count)
