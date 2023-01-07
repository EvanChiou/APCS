x,y = input().split()
for i in range(int(x)):
    count = 0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = a+b
    c.sort()
    if(c == list(set(c))):
        print(0)
        continue
    count = len(set(a).intersection(set(b)))
    print(count)