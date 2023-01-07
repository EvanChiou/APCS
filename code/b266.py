x = list(map(int,input().split(' ')))
y = []
z = []
def turn():
    a = y
    b = []
    for u in range(len(a[1])):
        b.append([])
        for i in range(len(a)):
            b[u].append(a[(i+1)*-1][u])
    return b
def flip():
    y.reverse()
    return y
for i in range(x[0]):
    y.append(list(map(int,input().split(' '))))
z = list(map(int,input().split(' ')))
for u in range(x[2]):
    if(z[u] == 0):
        y = turn()
    elif(z[u] == 1):
        y = flip()
for s in range(len(y)):
    y[s] = list(map(str,y[s]))
print(len(y),len(y[0]))
for a in y:
    z = " ".join(a)
    print(z)




