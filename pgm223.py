# extract the unique value of the list
import random
n=int(input('n=?'))
a=[random.randint(0,10)for i in range(n)]
print(a)
b=set(a)
print(len(b))
print(b)
m=[]
for i in b:
    d=[]
    c=a.count(i)
    d.append(i)
    d.append(c)
    m.append(d)
print(m)
