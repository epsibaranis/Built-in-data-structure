# copy the last n-character
s1=input('s1=?')
s2=''
n=int(input('n=?'))
s2=s1[-1:-n:-1]
print("copy the last n-character using string slicing",s2)