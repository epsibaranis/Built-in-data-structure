# n-Random integer no print it one by one
import random
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=random.randint(-100,100)
    a.append(x)
    i+=1
i=0
while i<n:
    print(a[i])
    i+=1
