x = [100,input()]
z = int(input())
y = [100]+input().split(' ')
round = 1
win = 0
def winner(a):
    if(a == '0'):return'2','5'
    if(a == '2'):return'5','0'
    if(a == '5'):return'0','2'
for i in range(1,z+1):
    c,k = winner(x[i])
    if(y[i] == c):win = 'Won';break
    if(y[i] == k):win = 'Lost';break
    if(y[i] == x[i]):
        c,k = winner(y[i])
        if(y[i] == y[i-1]):x.append(k);
        else:
            x.append(y[i])
    round+=1
x.pop(0)
if(win!='Won'and win!="Lost"):win = 'Drew';x.pop(z);round-=1
print(' '.join(x),":",win,"at round",round)