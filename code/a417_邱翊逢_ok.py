def pt(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print("%5d" % a[i][j], end = '')
        print('')
x = int(input())
for i in range(x):
    #
    # 變數命名建議參考題目的輸入說明
    # 後續 debug 時，比較不會因為變數名稱不同而混淆
    #
    a,b = list(map(int,input().split()))
    y = []
    ct = 0
    for u in range(a):
        y.append([])
        for j in range(a):
            y[u].append('')
    if(b == 1):
        #
        # u 作為二維陣列計算索引值順序
        # 由於此題掃描移動的方式不規則，建議i, j 方向各使用一個變數控制移動後的位置
        # 常見用於二維陣列索引值的變數設計名稱 (i, j) (x, y) (r, c)
        #
        for u in range(a-1):
            n = ct
            for j in range(a-1-u*2):
                y[u][j+u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[j+u][a-1-u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u][a-1-u-j] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-j-u][u] = j+1+n
                ct+=1
        if(a%2!=0):
            #
            # 直接在索引值位置中進行運算是很危險的
            # 容易發生 RE 或 out of list range 錯誤
            # 然後找不到錯誤在哪裡
            #
            y[((a+1)//2)-1][((a+1)//2)-1] = ct+1
        pt(y)
    else:
        for u in range(a-1):
            n = ct
            for j in range(a-1-u*2):
                y[j+u][u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u][j+u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[a-1-u-j][a-1-u] = j+1+n
                ct+=1
            n = ct
            for j in range(a-1-u*2):
                y[u][a-1-j-u] = j+1+n
                ct+=1
        if(a%2!=0):
            y[((a+1)//2)-1][((a+1)//2)-1] = ct+1
        pt(y)
