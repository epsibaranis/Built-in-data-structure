# Index of the biggest element
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i+=1
b=0
i=0
while i<n:
    if a[i]>b:
        b=a[i]
        p=i
    i+=1
print(p)


