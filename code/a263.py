while(True):
    try:
        cd = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
        x1 = list(map(int,input().split()))
        x2 = list(map(int,input().split()))
        def year(a):
            a = a-1
            y = a*365
            a = a//4 - a//100 + a//400
            y+=a
            return y
        def yn(a):
            if(a%4==0):
                if(a%100!=0):
                    return True
                elif(a%400==0):
                    return True
            return False
        def month(a,b):
            b=b-1
            ct=0
            if(yn(a)):c=cd[1]
            else:c=cd[0]
            for i in range(b):
                ct+=c[i]
            return ct
        xx1 = year(x1[0])+month(x1[0],x1[1])+x1[2]
        xx2 = year(x2[0])+month(x2[0],x2[1])+x2[2]
        ans = abs(xx1-xx2)
        print(ans)
    except:
        break