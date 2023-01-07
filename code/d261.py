while(True):
    try:
        x = int(input())
        if(x<0):break
        m = 0
        w = 1
        for i in range(x):
            ma = m+w
            wa = 1+m
            m = ma
            w = wa
        print(m,w+m)
    except:
        break