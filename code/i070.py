x = int(input())
teacher = list(map(int,input().split()))
child = list(map(int,input().split()))
lst = []
for i in range(x):
    if(teacher[i] in child):
        half_ = child[i+1:]
        _half = child[:i+1]
        if(teacher[i] in half_ and teacher[i] not in _half):
            lst.append(half_.index(teacher[i])+1)
        elif(teacher[i] in _half and teacher[i] not in half_):
            _half.reverse()
            idx = (_half.index(teacher[i])+1)*-1
            lst.append(idx)
        elif(teacher[i] in _half and teacher[i] in half_):
            indx1 = half_.index(teacher[i])+1
            _half.reverse()
            indx2 = (_half.index(teacher[i])+1)*-1
            lst.append(max(indx1,indx2))
    else:lst.append(-1)
print(*lst)
            