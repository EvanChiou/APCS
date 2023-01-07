ct = 0
while(True):
    try:
        ct+=1
        x = int(input())
        if(x<0):break
        y1 = list(map(int,input().split()))
        y2 = list(map(int,input().split()))
        print('Case ',ct,':',sep = '')
        for i in range(12):
            if(x-y2[i]<0):
                print('No problem. :(')
            else:
                x = x-y2[i]
                print('No problem! :D')
            x+=y1[i]
    except:
        break