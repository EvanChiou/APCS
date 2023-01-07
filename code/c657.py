while(True):
    try:
        x = list(input())
        ct = 1
        rc = ['',0]
        for i in range(1,len(x)):
            if(x[i] == x[i-1]):
                ct+=1
            else:   
                if(ct>rc[1]):
                    rc = [x[i-1],ct]
                ct = 1
        if(ct>rc[1]):
            rc = [x[-1],ct]
        print(f'{rc[0]} {rc[1]}')
    except:
        break