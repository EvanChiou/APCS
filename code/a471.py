def fuk(a,b):
    max = ((a-b+1)*(a+b))//2
    return [max,a]
while(1==1):
    try:
        answers = []
        N = int(input())
        cant = True
        for i in range(1,N//2+2):
            y = [fuk((N-i)//8+1+i,i),fuk((N-i)//4+1+i,i),fuk((N-i)//8+(N-i)//4+1+i,i),fuk((N-i)//2+1+i,i),[N,0],[0,i]]
            y.sort()
            a = y[y.index([N,0])-1][1]
            b = y[y.index([N,0])+1][1]
            j = a
            add = False
            while(j < b+1):
                an = fuk(j,i)
                if(an[0] == N):
                    cant = False
                    answers.append([i,j])
                    break
                else:
                    j+=1
        if(cant):print('No Solution...')
        else:
            for i in answers:
                print(i[0],'-',i[1],sep = '')
    except:
        break