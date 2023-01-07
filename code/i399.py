num = list(map(int,input().split()))
count = 0
for i in num:
    if(num.count(i)>count):
        count = num.count(i)
num = list(set(num))
num.sort(reverse=True)
print(count,*num)