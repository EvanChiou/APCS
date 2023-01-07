x = int(input())
y = list(map(int,input().split(' ')))
a = 0
b = 100
for i in y:
    if(i<60 and i>a):
        a = i
    elif(i>60 and i<b):
        b = i
y.sort()
y = list(map(str,y))
print(' '.join(y))
if(a == 0):
    print('best case')
else:
    print(a)
if(b == 100):
    print('worst case')
else:
    print(b)
