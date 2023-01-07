n,m = map(int,input().split())
aalist = list(map(int,input().split()))
bblist = list(map(int,input().split()))
st = list(map(int,input().split()))
fail = [0,0,0,0]
comp = st.copy()
while(len(comp)!= 1):
    print(comp)
    score = []
    for i in comp:
        score.append(aalist[i-1]*bblist[i-1])
    w,l = [],[]
    alist,blist = aalist.copy(),bblist.copy()
    for i in range(len(comp)//2):
        a,b = score[i*2],score[i*2+1]
        if(a>=b):
            aalist[comp[i*2]-1] = alist[comp[i*2]-1]+(alist[comp[i*2+1]-1]*blist[comp[i*2+1]-1])//(2*blist[comp[i*2]-1])
            bblist[comp[i*2]-1] = blist[comp[i*2]-1]+(alist[comp[i*2+1]-1]*blist[comp[i*2+1]-1])//(2*alist[comp[i*2]-1])
            aalist[comp[i*2+1]-1] = alist[comp[i*2+1]-1] + alist[comp[i*2+1]-1]//2
            bblist[comp[i*2+1]-1] = blist[comp[i*2+1]-1] + blist[comp[i*2+1]-1]//2
            fail[comp[i*2+1]-1]+=1
            w.append(comp[i*2]);l.append(comp[i*2+1])
        elif(b>a):
            aalist[comp[i*2+1]-1] = alist[comp[i*2+1]-1]+(alist[comp[i*2]-1]*blist[comp[i*2]-1])//(2*blist[comp[i*2+1]-1])
            bblist[comp[i*2+1]-1] = blist[comp[i*2+1]-1]+(alist[comp[i*2]-1]*blist[comp[i*2]-1])//(2*alist[comp[i*2+1]-1])
            aalist[comp[i*2]-1] = alist[comp[i*2]-1] + alist[comp[i*2]-1]//2
            bblist[comp[i*2]-1] = blist[comp[i*2]-1] + blist[comp[i*2]-1]//2
            fail[comp[i*2]-1]+=1
            w.append(comp[i*2+1]);l.append(comp[i*2])
    comp = w+l
    for i in comp:
        if(fail[i-1]>=m):
            comp.remove(i)
print(comp[0])
        
