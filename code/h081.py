a,b,c = list(map(int,input().split(' ')))
print(a,b,c)
if(a+b<c):
    print("No")
elif(a**2+b**2 == c**2):
    print("Right")
elif(a**2+b**2 < c**2):
    print("Obtuse")
elif(a**2+b**2 > c**2):
    print("Acute")