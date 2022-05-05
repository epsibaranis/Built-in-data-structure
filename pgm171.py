# -*- coding: utf-8 -*-
"""
pgm no 171
Created on Mon Jan 10 09:21:26 2022
copy the n character from the end
@author: tt
"""
s1=input('s1=?')
n=int(input('n=?'))
s2=''
l=len(s1)
for i in range(l-1,n+1,-1):
   s2=s2+s1[i]
print(s2)



