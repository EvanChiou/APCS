x = [int(input())]
y = input()
z = list(map(int,input().split(' ')))
final = 0
count = 0
xcount = 0
while(count<len(z)):
    if(x[count] == 0 and z[count] == 2):break
    elif(x[count] == 0 and z[count] == 5):final = 1;break
    elif(x[count] == 2 and z[count] == 0):final = 1;break
    elif(x[count] == 2 and z[count] == 5):break
    elif(x[count] == 5 and z[count] == 0):break
    elif(x[count] == 5 and z[count] == 2):final = 1;break
    if(len(x) !=1 and z[count-1] == z[count]):
        if(z[count] == 0):x.append(5)
        elif(z[count] == 2):x.append(0)
        else:x.append(2)
    else:
        x.append(z[count])
    count +=1
if(count >= len(z)):
    x.pop()
    for i in x:
        print(i,end = ' ')
    print(": Drew at round",count)
    final = 10
if(final == 0):
    for i in x:
        print(i,end = ' ')
    print(": Won at round",count+1)
elif(final == 1):
    for i in x:
        print(i,end = ' ')
    print(": Lost at round",count+1)
