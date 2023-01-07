xxx = [7,5,3,1,2,4,6,8]
x = int(input())
if(x%8 == 0):
    t = x//8
else:
    t = x//8+1
y = []
z = []
y1 = []
for i in range(t):
    z.append([])
tn = 0
ct = 0
for i in range(x):
    a,b = input().split()
    a = int(a)
    b = float(b)
    y.append([b,a])
y.sort()
for i in range(1,x+1):
    ct+=1
    if(tn%2 == 0):
        if(i%t == 0):
            z[t-1].append(y[i-1])
        else:
            z[(i%t)-1].append(y[i-1])
    else:
        if(i%t == 0):
            z[0].append(y[i-1])
        else:
            z[t-i%t].append(y[i-1])
    if(ct == t):tn+=1;ct = 0
for i in range(t):
    y1.append([[0,i+1]])
    for u in range(8):
        if(xxx[u]-1<len(z[i])):
            y1[i].append(z[i][xxx[u]-1])
for i in range(len(y1)):
    for u in range(len(y1[i])):
        print(y1[i][u][1],end = ' ')
    print()