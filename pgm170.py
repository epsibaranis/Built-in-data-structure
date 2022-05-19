# Delete all the vowels in a string
s1=input('s1=?')
s2=''
l=len(s1)
for i in range(l):
  if s1[i]=='a'or s1[i]=='A'or s1[i]=='e' or s1[i]=='E' or s1[i]=='i' or s1[i]=='I' or s1[i]=='o' or s1[i]=='O' or s1[i]=='u' or s1[i]=='U':
      pass
  else:
      s2=s2+s1[i]
print("Delete all the vowels in a string from a string:",s2)