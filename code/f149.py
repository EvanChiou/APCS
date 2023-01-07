x,y = list(map(int,input().split()))
ct = 0
cl = [[1,0],[1,1],[0,1],[-1,-1],[-1,0],[-1,1],[1,-1],[0,-1]]
def check(a,b):
    boom = 0
    er = False
    for i in cl:
        print(ground[a+i[0]][b+i[1]])
        if(ground[a+i[0]][b+i[1]] == 1):
            boom+=1
        elif(ground[a+i[0]][b+i[1]] == 5):
            er = True
        if(er):boom = 0
    return boom
ground = [[0]*(x+2)]
for i in range(x):
    ground.append(list(map(int,input().split())))
    ground[i+1].insert(0,0)
    ground[i+1].append(0)
    ct+=ground[i+1].count(1)
ground.append([0]*(x+2))
bm = 0
for i in ground:
    print(*i)
for i in range(1,x+1):
    for j in range(1,x+1):
        if(ground[i][j] == 5):
            bm+=check(i,j)
print(bm,ct-bm)

