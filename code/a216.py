while True:
    try:
        countf = 0
        countg = 0
        x = int(input())
        for i in range(1,x+1):
            countf += i
            countg +=countf
        print(countf,countg)

    except:
        break