while(True):
    try:
        n = int(input())
        m = int(input())
        mp = []
        for i in range(n):mp.append([])
        for i in range(m):
            x,y = map(int,input().split())
            mp[x].append(y)
            mp[y].append(x)
        def BFS(mpp,start):
            R = [start]
            visit = [0 for i in range(n)]
            while(len(R)>0):
                now = R.pop(0)
                for nx in mpp[now]:
                    if(visit[nx] == 0):
                        if(visit[now] == 1):
                            visit[nx] = 2
                        else:
                            visit[nx] = 1
                        R.append(nx)
                    elif(visit[nx] == visit[now]):
                        return False
            return True
        def DFS(mpp,start):
            visit = [0 for i in range(n)]
            visit[start] = 1
            for i in mpp[start]:
                if(visit[i] == 0):
                    if(visit[start] == 1):
                        visit[i] = 2
                    else:
                        visit[i] = 1
                    print(i)
                    if(not DFS(mpp,i)):return False
                elif(visit[i] == visit[start]):
                    return False
            return True
            
        if(BFS(mp,0)):
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
    except:
        break

