x,y,z = map(int,(input().split()))
arr = [[0 for j in range(y)] for i in range(x)]
def show(a):
    for i in a:
        print(*i)
def fill(r,t,e,ez,ps):
    if(ez):
        for i in range(r+1,t):
            if(e[i] != 9):
                e[i]+=1
        return e
    else:
        for i in range(r+1,t):
            if(e[i][ps] != 9):
                e[i][ps]+=1
        return e
def unf(r,t,e,ez,ps):
    if(ez):
        for i in range(r+1,t):
            if(e[i]>0):
                e[i]-=1
        return e
    else:
        for i in range(r+1,t):
            if(e[i][ps]>0):
                e[i][ps] -=1
        print(r,t,e)
        return e
def inp(r,t,e):
    mn = 10000
    for i in range(t):
        if(e[r][i] == 9):
            if(abs(i-t)<mn):mn = abs(i-t)
    if(mn!=10000):
        e[r] = fill(t-mn,t,e[r],True,0)
    mn = 10000
    for i in range(t+1,y):
        if(e[r][i] == 9):
            if(abs(i-t)<mn):mn = abs(i-t)
    if(mn!=10000):
        e[r] = fill(t,mn+t,e[r],True,0)
    mn = 10000
    for i in range(r):
        if(e[i][t] == 9):
            if(abs(i-r)<mn):mn = abs(i-r)
    if(mn!=10000):
        e = fill(r-mn,r,e,False,t)
    mn = 10000
    for i in range(r+1,x):
        if(e[i][t] == 9):
            if(abs(i-r)<mn):mn = abs(i-r)
    if(mn!=10000):
        e = fill(r,mn+r,e,False,t)
    e[r][t] = 9
    return e
def rmv(r,t,e):
    e[r][t] = 0
    mn = 10000
    for i in range(t):
        if(e[r][i] == 9):
            if(abs(i-t)<mn):mn = abs(i-t)
    if(mn!=10000):
        e[r] = unf(t-mn,t,e[r],True,0)
    mn = 10000
    for i in range(t+1,y):
        if(e[r][i] == 9):
            if(abs(i-t)<mn):mn = abs(i-t)
    if(mn!=10000):
        e[r] = unf(t,mn+t,e[r],True,0)
    mn = 10000
    for i in range(r):
        if(e[i][t] == 9):
            if(abs(i-r)<mn):mn = abs(i-r)
    if(mn!=10000):
        e = unf(r-mn,r,e,False,t)
    mn = 10000
    for i in range(r+1,x):
        if(e[i][t] == 9):
            if(abs(i-r)<mn):mn = abs(i-r)
    if(mn!=10000):
        e = unf(r,mn+r,e,False,t)
    return e
for i in range(z):
    a,b,c = map(int,input().split())
    if(c == 0):
        arr = inp(a,b,arr)
        show(arr)
    else:
        arr = rmv(a,b,arr)
        show(arr)