while(True):
    try:
        x = int(input())
        if(x == -1):break
        y = list(map(int,input().split()))
        ct = 0
        for i in range(x-1):
            y.sort()
            ct+=y[0]+y[1]
            y.append(y[0]+y[1])
            y.pop(0);y.pop(0)
        print(ct)
    except:
        break 