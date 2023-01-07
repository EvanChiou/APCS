while(1==1):
    try:
        x = list(map(int,input().split()))
        y = []
        tn = []
        for i in range(x[0]):
            y.append(input().split())
        for i in range(x[1]):
            tn.append([])
            for j in range(x[0]):
                tn[i].append(y[j][i])
            print(' '.join(tn[i]))
    except:
        break
