import re


while(1==1):
    try:
        x = list(map(ord,list(input())))
        y = []
        u = 0
        x.sort()
        while(u!=len(x)):
            z = x.count(x[u])
            y.append([z,x[u]])
            u+=z
        y.sort(reverse=True)
        for i in y:
            print(i[1],i[0])
    except:
        break