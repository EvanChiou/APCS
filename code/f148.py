x,y = list(map(int,input().split()))
z = int(input())
ar = []
point = []
for i in range(x):
    ar.append(input().split())
    for j in ar[i]:
        if(j!='0'):
            point.append([j,i,ar[i].index(j)])
point.sort()
if(len(point)>=z):
    for i in range(z):
        print(point[i][1],point[i][2])
else:
    print("Mission fail.")