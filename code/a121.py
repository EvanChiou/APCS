try:
    while(True):
        x,y = input().split(' ')
        x = int(x)
        y = int(y)
        count = 0
        if(y-x>0):
            if(x%2==0):
                for i in range(x+1,y+1,2):
                    for u in range(1,i+1,2):
                        if(i%u==0 and u!=i and u!=1):
                            count-=1
                            break
                    count+=1
            else:
                for i in range(x,y+1,2):
                    for u in range(1,i+1,2):
                        if(i%u==0 and u!=i and u!=1):
                            count-=1
                            break
                    count+=1
            print(count)
        else:
            print(0)
except:
    pass

