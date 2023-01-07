count = 0
while(True):
    try:
        x = int(input())
        if(x==0):break
        count+=1
        y = list(map(int,input().split()))
        z = sum(y)//x
        w = 0
        for i in y:
            if(i>z):w+=(i-z)
        print("Set #",count,sep = '')
        print("The minimum number of moves is ",w,".",sep = '')
    except:
        break
