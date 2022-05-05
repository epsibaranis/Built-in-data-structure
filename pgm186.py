# index in the biggest and smallest element in the list
import random
a=[]
n=int(input('n=?'))
for i in range(n):
    x=random.randint(0,10000)
    a.append(x)
print(a)
b=max(a)
s=min(a)
p1=a.index(b)
p2=a.index(s)
print(b)
print(s)
print(p1)
print|(p2)
           