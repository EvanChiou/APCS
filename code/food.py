while(True):
    try:
        n,e = map(int,input().split())
    except:break
    food = n*e
    day = 0
    while(food>0):
        g = food/e
        if(g>int(g)):g = int(g)+1
        else:g = int(g)
        food-=g
        day+=1
    print(day)