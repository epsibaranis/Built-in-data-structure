# difference of two n*n by matrix using list comprehension
import random
n=int(input('n=?'))
a=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print(a)
b=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print(b)
c=[[a[i][j]-b[i][j]for j in range(n)]for i in range(n)]
print(c)

