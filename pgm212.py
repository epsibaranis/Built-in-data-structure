# Sum of two n*n by matrix using list comprehension
import random
n=int(input('n=?'))
x=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print(x)
y=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print(y)
z=[[x[i][j]+y[i][j]for j in range(n)]for i in range(n)]
print(z)

