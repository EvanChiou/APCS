x = int(input())
y = [x]
def fuk(a):
    if a == 1:
        return 1
    elif a%2 == 0:
        return fuk(a/2)
    else:
         return fuk(a-1) + fuk(a+1)
while(y.count(1) != len(y)):
    yy = []
    for i in range(len(y)):
        if(y[i] == 1):
            yy.append(1)
        elif(y[i] % 2 == 0):
            yy.append(y[i]/2)
        else:
            yy.append(y[i]+1)
            yy.append(y[i]-1)
    y = yy.copy()
print(int(sum(y)))
