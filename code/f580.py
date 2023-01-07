n,m = map(int,input().split())
dices = []
def right(lst):
    lst.insert(0,lst[-1])
    lst.pop()
    return lst
def front(lst):
    dupe = []
    for i in lst:
        dupe.append(i[1])
    dupe = right(dupe)
    for i in range(3):
        lst[i][1] = dupe[i]
    return lst
def change(lst,a,b):
    lst.insert(a,lst[b])
    lst.insert(b+1,lst[a+1])
    lst.pop(a+1)
    lst.pop(b+1)
    return lst
for i in range(n):
    dices.append([[0,3,0,0],[5,1,2,6],[0,4,0,0]])
for i in range(m):
    ob,ac = map(int,input().split())
    ob-=1
    if(ac > 0):
        lst = [ob,ac-1]
        lst.sort()
        dices = change(dices,lst[0],lst[1])
    elif(ac == -1):
        dices[ob] = front(dices[ob])
    elif(ac == -2):
        dices[ob][1] = right(dices[ob][1])
    print(dices[0][1][1])
    print(dices[0])
cout = []
for i in range(n):
    cout.append(dices[i][1][1])
print(*cout)


