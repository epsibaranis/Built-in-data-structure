# list of n elements
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i=i+1
m=0
print("print the list element by element")
while m<n:
    print (a[m])
    m=m+1
