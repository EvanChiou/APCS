x = list(map(int,input().split(' ')))
y = list(map(int,input().split(' ')))
z = int(input())
largest = 0
for i in range(z+1):
    first = x[0]*(i**2) + x[1]*i + x[2]
    second = y[0]*((z-i)**2) + y[1]*(z-i) + y[2]
    if(first + second >largest):
        largest = first + second
print(largest)