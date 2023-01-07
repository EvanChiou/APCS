x = int(input())
y = []
count = 0
sett = []
for i in range(x):
    y.append(input())
for i in range(len(y)):
    for u in range(1,len(y)):
        if(y[i]!=y[u]):
            if((len(y[i])+len(y[u]))%2==0):
                a = list(y[i]) + list(y[u])
                b = int(len(a)/2)
                if(a[:b] == a[b:]):
                    if({i,u} in sett):
                        count+=0
                    else:
                        count+=1
                        sett.append({i,u})
print(count)
                
