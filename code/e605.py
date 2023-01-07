count = 0
while(True):
    try:
        count+=1
        scan = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        x,y = map(int,input().split())
        if(x == 0):break
        maps = [['.']*(y+2)]
        def check(arr,a,b):
            count = 0
            for i in scan:
                if arr[a+i[0]][b+i[1]] == '*':
                    count+=1
            return count
        for i in range(x):
            maps.append(list(input()))
            maps[i+1].insert(0,'.')
            maps[i+1].append('.')
        maps.append(['.']*(y+2))
        ans = []
        for i in range(1,x+1):
            ans.append([])
            for j in range(1,y+1):
                if(maps[i][j] != '*'):
                    ans[i-1].append(str(check(maps,i,j)))
                else:
                    ans[i-1].append('*')
        print(f'Field #{count}:')
        for i in ans:
            print(''.join(i))
    except:
        break
