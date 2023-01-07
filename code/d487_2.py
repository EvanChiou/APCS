x = int(input())
y = 1
z = []
while(x!=0):
    y*=x
    z.append(str(x))
    x-=1
if(len(z) == 0):z.append(1)
print(f'{x}! =',' * '.join(z),f'= {y}')