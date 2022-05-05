# n by n matrix
import random
n=int(input('n=?'))
a=tuple(tuple(random.randint(0,10)for j in range(n))for i in range(n))
print(a)