def pt(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print("%5d" % a[i][j], end = '')
        print('')
x = int(input())
for i in range(x):
    a,b = list(map(int,input().split()))
    y = []
    ct = 0
    for u in range(a):
        y.append([])
        for j in range(a):
            y[u].append('')
    if(b == 1):
        for u in range(a-1):
            n = ct
            for j in range(a-1-u*2):
                y[u][j+u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[j+u][a-1-u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u][a-1-u-j] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-j-u][u] = j+1+n
                ct+=1
        if(a%2!=0):
            y[((a+1)//2)-1][((a+1)//2)-1] = ct+1
        pt(y)
    else:
        for u in range(a-1):
            n = ct
            for j in range(a-1-u*2):
                y[j+u][u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u][j+u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u-j][a-1-u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[u][a-1-j-u] = j+1+n
                ct+=1
        if(a%2!=0):
            y[((a+1)//2)-1][((a+1)//2)-1] = ct+1
        pt(y)