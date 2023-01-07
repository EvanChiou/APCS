x = int(input())
input()
y = []
for i in range(x):
    y.append([int(input()),int(input())])
    for u in range(y[i][1]):
        for j in range(1,y[i][0]+1):
            for g in range(j):
                print(j,end='')
            print('')
        for j in range(1,y[i][0]):
            for g in range(y[i][0]-j):
                print(y[i][0]-j,end='')
            print('')