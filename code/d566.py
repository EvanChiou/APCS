x = int(input())
ur = []
sc = []
ct = 0
kl = 0
for i in range(x):
    y = input().split()
    if(y[0] in ur):
        if('AC' in sc[ur.index(y[0])]):
            pass
        else:
            sc[ur.index(y[0])].append(y[1])
            if(y[1] == 'AC'):ct+=1
    else:
        ur.append(y[0])
        sc.append([y[1]])
        if(y[1] == 'AC'):ct+=1
for i in range(len(ur)):
    if('AC' in sc[i]):
        if(sc[i].index('AC') == 0):
            kl+=1
if(kl == ct):
    print("0%")
else:
    print(int((kl/ct)*100),'%',sep='')
