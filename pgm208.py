# construct alist of n random numbers and extract even numbers from the zero
import random
random.seed(0)
n=int(input('n=?'))
a=[random.randint(0,10)  for i in range(n)]
print(a)
b=[i for i in a if i%2==0]
print(b)
