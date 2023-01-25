x = int(input())
if(x==1):print(1)
num = 2
ft = True
while(x!=1):
    ct = 0
    while(True):
        if(x%num == 0):ct+=1;x=x//num
        else:break
    if(ft and ct!=0):
        if(ct==1):
            print(num,end='');ft=False
        else:
            print(num,'^',ct,sep='',end='');ft=False
    elif(ct!=0):
        if(ct==1):
            print(' *',num,end='')
        else:
            print(' * ',num,'^',ct,sep='',end='')
    num+=1
