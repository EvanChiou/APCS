count = 0
x = int(input())
y = []
z = []
a = 0
b = 1000000000000000000000
for i in range(x):
    y.append(list(map(int,input().split(' '))))
    if(y[i][0]>a):
        a = y[i][0]
    elif(y[i][0]<b):
        b = y[i][0]
    if(y[i][1]>a):
        a = y[i][1]
    elif(y[i][1]<b):
        a = y[i][1]
for u in range(b,a+1):
    z.append(u)
print(z)
for s in y:
    j = s[1]-s[0]
    for h in range(j):
        z[s[0]-b+h] = 0
for p in z:
    if(p==0):count+=1
print(z)
print(count)