# -*- coding: utf-8 -*-
"""
pgm no 172
Created on Mon Jan 10 09:53:21 2022
copy n character from the end
@author: tt
"""
s1=input('s1=?')
m=int(input('m=?'))
n=int(input('n=?'))
s2=''
k=m+n
for i in range(-m,-k,-1):
    s2=s2+s1[i]
print(s2)


