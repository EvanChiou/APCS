z = int(input())
x = list(map(int,input().split()))
y = int(input())-1
ft = True
while(True):
    if(y!=z-1 and y!= 0):
        if(x[y+1]<x[y-1] and ft):
            y+=1
            tn = True
            ft = False
        elif(ft):
            y-=1
            tn = False
            ft = False
        if(tn and x[y+1]<=x[y]):
            y+=1
        elif(tn==False and x[y-1]<=x[y]):
            y-=1
        else:
            break
    else:
        if(ft):
            if(y==0):
                if(x[y+1]<x[y]):
                    y+=1
                    ft = False
                    tn = True
            elif(y==z-1):
                if(x[y-1]<x[y]):
                    y-=1
                    ft = False
                    tn = False
        else:break
print(y+1)