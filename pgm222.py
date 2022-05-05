# extract the unique value of the list
import random
n=int(input('n=?'))
a=[random.randint(0,100)for i in range(n)]
print(a)
b=set(a)
print(len(b))
print(b)
for i in b:
    print('count of the element',i,'=',a.count(i))
