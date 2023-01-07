x = list(input())
x.reverse()
a = 0
b = 0
for i in range(len(x)):
    if((i+1)%2 == 0):a = a+int(x[i])
    else:b = b+int(x[i])
c = a-b
if(c<0):print(c*-1)
else:print(c)