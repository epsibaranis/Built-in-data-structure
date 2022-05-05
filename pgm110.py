# Smallest no in n-element list
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i=i+1
b=9999999999
i=0
while i<n:
    if b>a[i]:
        b=a[i]

    i+=1
print(b)


