# List of n students Bio-data
n=int(input('n=?'))
b=[]
i=0
while i<n:
       a=[]
       x=input('Name   : ')
       y=input('Age    : ')
       c=input('Gender : ')
       d=input('Address: ')
       e=input('Emailid: ')
       a.append(x)
       a.append(y)
       a.append(c)
       a.append(d)
       a.append(e)
       b.append(a)
       i+=1
print('List of students Bio-data: ',b)
