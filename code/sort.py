x = list(map(int,list(input())))
def xx(lst):
    if(lst == []):return 0
    if(len(lst) == 4):
        if(lst[0] == 0):a = str(lst[1])
        else:a = str(lst[0]*lst[1])
        if(lst[2] == 0):b = str(lst[3])
        else:b = str(lst[2]*lst[3])
        if(a == '0'):a = ''
        if(b == '0'):b = ''
        return xx(list(map(int,list(a+b))))
    elif(len(lst) == 3):
        if(lst[0] == 0):a = str(lst[1])
        else:a = str(lst[0]*lst[1])
        if(lst[1] == 0):b = str(lst[2])
        else:b = str(lst[1]*lst[2])
        if(a == '0'):a = ''
        if(b == '0'):b = ''
        return xx(list(map(int,list(a+b))))
    elif(len(lst) == 2):
        return xx(list(map(int,list(str(lst[0]*lst[1])))))
    elif(len(lst) == 1):
        return lst[0]
print(xx(x))

