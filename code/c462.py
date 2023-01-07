x = int(input())
y = list(input())
i = 1
rcc = 0
def strike(a):
    yy = y.copy()
    for i in range(a):
        yy.pop(0)
    case = yy[0].isupper()
    rc = 0
    while(True):
        try:
            ct = 1
            if(case is yy[0].isupper()):
                for i in range(1,x):
                    if(case is yy[i].isupper()):
                        ct+=1
            else:
                return rc
            if(ct == x):rc+=x
            else:return rc
            case = not case
            for i in range(x):
                yy.pop(0)
        except:
            return rc
while(len(y)!=0):
    if(strike(0)>rcc):
        rcc = strike(0)
    for j in range(1,strike(0)-x):
        y.pop(0)
    y.pop(0)
print(rcc)

