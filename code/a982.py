x = int(input())
y = []
for i in range(x):
    y.append(list(input()))
def check(a,lc,dr):
    ch = []
    if(a[lc[0]+1][lc[1]] == '.' and dr!=3):
        ch.append(1)
    if(a[lc[0]][lc[1]+1] == '.' and dr!=4):
        ch.append(2)
    if(a[lc[0]-1][lc[1]] == '.' and dr!=1):
        ch.append(3)
    if(a[lc[0]][lc[1]-1] == '.' and dr!=2):
        ch.append(4)
    return ch
def step(a):
    if(a == 1):
        return [1,0]
    elif(a == 2):
        return [0,1]
    elif(a == 3):
        return [-1,0]
    elif(a == 4):
        return [0,-1]
def path(a,lc,cs,dr):
    ch = check(a,lc,dr)
    if(ch>=1):
        lc=list(map(lambda x :x[0]+x[1] ,zip(lc,step(ch[0]))))
        if(ch>1):
            cs.append
    elif(ch == 0):
        cs

    



