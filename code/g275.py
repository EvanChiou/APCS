for i in range(int(input())):
    x = input().split()
    y = input().split()
    Non = 0
    if(x[1] == x[3] or x[1] != x[5] or y[1] == y[3] or y[1] != y[5]):
        print("A",end = '')
    else:Non+=1
    if(x[6] != '1' or y[6] !='0'):
        print("B",end = '')
    else:Non+=1
    if(x[1] == y[1] or x[3] == y[3] or x[5] == y[5]):
        print("C",end = '')
    else:Non+=1
    if(Non == 3):
        print("None")
    else:print('')