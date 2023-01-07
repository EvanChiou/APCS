x = int(input())
y = []
over = []
count = 0
for i in range(x):
    y.append(list(map(int,input().split())))
    if(y[i][1]>100):count+=(y[i][1]-100)*5;over.append(y[i][0])
over.sort()
if(over!=[]):print(*over)
print(count)