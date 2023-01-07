import time
average = []
x = int(input())
for q in range(3):
    start_time = time.time()
    for i in range(2,x+1):
        nah = True
        for j in range(2,i):
            if(i%j==0):
                nah = False
                break
        if(nah):print(i)
    end_time = time.time()
    dura = end_time-start_time
    average.append(dura)
print(sum(average)/3)

