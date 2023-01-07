import time
average = []
x = int(input())
yy = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for q in range(3):
    y = yy.copy()
    print(y)
    start_time = time.time()
    for i in y:
        if(i<=x):
            print(i)
    if(x<=100):break
    for i in range(101,x,2):
        nah = True
        half = i//2
        for j in y:
            if(j>half):break
            if(i%j == 0):
                nah = False
                break
        if(nah):y.append(i);print(i)
    end_time = time.time()
    dura = end_time-start_time
    average.append(dura)
print(sum(average)/3)