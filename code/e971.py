x,y = list(map(int,input().split()))
picture = []
for i in range(x):
    picture.append(list(map(int,input().split())))
    color = False
    que = []
    for j in range(y):
        z = picture[i][j]
        if(z == 1):
            if(len(que) != 0):
                for u in que:
                    picture[i][u] = 1
                que = []
            color = not color
        elif(z == 0 and color):
            que.append(j)
for i in picture:
    print(*i)
        