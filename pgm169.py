#copy the last n-character
s1=input('s1=?')
n=int(input('n=?'))
l=len(s1)
m=l-n
s2=''
s2=s1[m:l]
print("copy the last n-character",s2)