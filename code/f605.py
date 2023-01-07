from tkinter import Y


x = list(map(int,input().split(' ')))
count = 0
price = 0
for i in range(x[0]):
    y = list(map(int,input().split(' ')))
    if((max(y)-min(y))>=x[1]):count+=1 ; price+=sum(y)/3
print(count,price)
    
