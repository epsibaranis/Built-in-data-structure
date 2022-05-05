# construct a list of n elements and print it reverse order
a=[]
n=int(input('n=?'))
for i in range(n):
    x=input('x=?')
    a.append(x)
print(a)
for i in range(-1,-n-1,-1):
    print(a[i])
