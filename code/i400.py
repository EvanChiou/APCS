m,n = map(int,input().split())
step = []
for i in range(m):
    step.append(list(input()))
text = list(input())
for i in range(m):
    ct = step[-1].count('1')
    tt = []
    for j in range(n):
        if(step[-1][-1] == '1'):
            tt.append(text[-1])
        else:
            tt.insert(0,text[-1])
        text.pop()
        step[-1].pop()
    text = tt
    step.pop()
    if(ct%2!=0):
        a = text[:(n//2)]
        c = []
        cc = 0
        if(n%2!=0):c = [text[n//2]];cc = 1
        b = text[(n//2)+cc:]
        text = b+c+a
for i in text:
    print(i,end = '')