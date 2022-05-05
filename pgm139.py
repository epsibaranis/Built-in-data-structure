# Number is Leap Year or Not in between the limits
a=int(input('a='))
b=int(input('b='))
for i in range (a+1,b):
    if i%4==0:
     print('Leap Year',i)
    else:
     print('Not Leap Year',i)

