# copy n character from the end
s1=input('s1=?')
m=int(input('m=?'))
n=int(input('n=?'))
s2=''
k=m+n
for i in range(-m,-k,-1):
    s2=s2+s1[i]
print("copy n character from the end in a string using slicing",s2)