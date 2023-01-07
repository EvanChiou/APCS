x,y = map(int,input().split())
cards = list(map(int,input().split()))
def wash(lst):
    num = len(lst)//2
    a = lst[:num]
    b = lst[num:]
    c = []
    for i in range(num):
        c.append(a[i])
        c.append(b[i])
    return c
for i in range(y):
    cards = wash(cards)
print(*cards)