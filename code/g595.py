input()
count = 0
x = list(map(int,input().split(' ')))
for i in range(len(x)):
    if(x[i] == 0):
        if(i == 0):
            x[i] = x[i+1]
        elif(i == len(x)-1):
            x[i] = x[i-1]
        else:
            if(x[i+1]>x[i-1]):
                x[i] = x[i-1]
            else:
                x[i] = x[i+1]
        count+=x[i]
print(count)
        
        
