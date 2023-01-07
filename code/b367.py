x = int(input())
for i in range(x):
    o = list(map(int,input().split()))
    y = []
    y1 = []
    for j in range(o[0]):
        y.append(input().split())
    for j in range(o[0]):
        y1.append([])
        for u in range(o[1]):
            y1[j].append(y[(o[0]-1)-j][(o[1]-1)-u])
    if(y == y1):
        print('go forward')
    else:
        print('keep defending')