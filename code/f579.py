x = input().split(' ')
y = int(input())
count = 0
for i in range(y):
    y = input().split(' ')
    if(x[0] in y and x[1] in y):
        count +=1
print(count)