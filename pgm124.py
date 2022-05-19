# Sum of elements of each row in a list of n by n matrix
import random
n=int(input('n=?'))
b=[]
i=0
while i<n:
    r=0
    a=[]
    while r<n:
        x=random.randint(0,1000)
        a.append(x)
        r+=1
    b.append(a)
    i+=1
print("n*n matrixes",b)
i=0
while i<n:
    j=0
    s=0
    while j<n:
        s=s+b[j][i]
        j+=1
    print('Sum of the elements in a row of n by n matrix',s)
    i+=1