# two sets of n random numbers and their union intersection difference
import random
n=int(input('n=?'))
a=set()
b=set()
for i in range(n):
    a.add(random.randint(0,10))
    b.add(random.randint(0,10))
print(a)
print(b)
print(a|b)
print(a&b)
print(a-b)


