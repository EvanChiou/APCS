x = int(input())
for i in range(x):
    count = 0
    a = int(input())
    b = list(map(int,input().split()))
    b.sort(reverse=True)
    cut = a//3
    j = 2
    while(cut>0 and j<=a-1):
        count+=b[j]
        j+=3
    print(count)