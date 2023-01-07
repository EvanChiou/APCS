while(True):
    try:
        x = list(map(int,input().split()))
        y = int(input())
        for i in range(y):
            x1 = []
            for u in x:
                x1.append(u)
            a = 0
            b = 0
            ch = list(map(int,input().split()))
            for u in range(4):
                if(x1[u]==ch[u]):
                    a+=1
                    x1[u] = 100
                    ch[u] = 1000
            for u in range(4):
                if(ch[u] in x1):
                    x1[x1.index(ch[u])] = 100
                    b+=1
            print(a,'A',b,'B',sep='')
                
    except:
        break