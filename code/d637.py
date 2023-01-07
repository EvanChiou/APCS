x = int(input())
y = []
eat = 100
pw = 0
a = 0
def sec(n):
    return n[1]
for i in range(x):
    y.append(list(map(int,input().split())))
    y[i] = [y[i][0],y[i][1]/y[i][0],y[i][1]]
y.sort(key=sec,reverse=True)
while(eat>=0):
    for i in y:
        if(eat>i[0]):
            eat-=i[0]
            pw+=i[2]
            y.remove(i)
    break
a = pw
print(pw)