while(1==1):
    try:
        x,y = map(int,input().split())
        print((x//y+x)//y+x)
    except:
        break