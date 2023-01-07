x = int(input())
y = []
for i in range(x):
    lst = list(input())
    y.append(int(lst[3]+lst[4]))
ys = set(y)
st = []
for i in ys:
    st.append([i,y.count(i)])
st.sort()
for i in st:
    print(*i)