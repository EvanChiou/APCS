x = int(input())
y = list(map(int,input().split()))
def bbs(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[i] >arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr
def mrs(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = mrs(arr[:mid])
    right = mrs(arr[mid:])
    return mrd(left,right)
def mrd(L,R):
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(L) and r_index < len(R):
        if L[l_index] <R[r_index]:
            result.append(L[l_index])
            l_index+=1
        else:
            result.append(R[r_index])
            r_index +=1
    result+=L[l_index:]
    result+=R[r_index:]
    return result
def qks(dt,lt,rt):
    if lt<rt:
        l = lt
        r = rt+1
        pv = dt[lt]
        while True:
            while l<rt:
                l+=1
                if dt[l]>=pv:
                    break
            while r>0:
                r-=1
                if dt[r]<=pv:
                    break
            if l>=r:
                break
            dt[l],dt[r] = dt[r],dt[l]
        dt[lt],dt[r] = dt[r],dt[lt]
        qks(dt,lt,r-1)
        qks(dt,r+1,rt)
print(*bbs(y))
y.sort