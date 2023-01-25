ak = [1, 10, 19, 28, 37, 46, 55, 64, 39, 73, 82, 2, 11, 20, 48, 29, 38, 47, 56, 65, 74, 83, 21, 3, 12, 30]
x = list(map(int,list(input())))
ans = []
ck = x[8]
x.pop()
sm = 0
for i in range(8):
    x[i] = x[i]*(8-i)
sm = sum(x)
nx = (sm//10)*10+(10-ck)
while(nx-sm<=83):
    if(nx-sm in ak):
        ans.append(nx-sm)
    nx+=10
for i in range(len(ans)):
    ans[i] = chr(ak.index(ans[i])+65)
ans.sort()
print(''.join(ans))
