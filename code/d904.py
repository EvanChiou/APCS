x,y = map(int,input().split())
z = []
for i in range(y):
    z.append(int(input()))
count = 0
z.sort(reverse=True)
def coin(n):
    global count
    for i in z:
        if(n>=i):
            count+=n//i
            return coin(n%i)
    return 0 
coin(x)
print(count)
