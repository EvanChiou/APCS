import sys
letter = {"0 1 0 1": "A",
          "0 1 1 1": "B",
          "0 0 1 0": "C",
          "1 1 0 1": "D",
          "1 0 0 0": "E",
          "1 1 0 0": "F"}
 
for i in sys.stdin:
    n = int(i)
    ans = ""
    for i in range(n):
        s = sys.stdin.readline().strip()
        ans += letter[s]
    print (ans)
'''
dic = {'0 1 0 1':'A','0 1 1 1':'B','0 0 1 0':'C','1 1 0 1':'D','1 0 0 0':'E','1 1 0 0':'F'}
while(True):
    try:
        y = []
        for i in range(int(input())):
            y.append(input())
        y = list(map(lambda a:dic[a],y))
        print(''.join(y))
    except:
        break
'''