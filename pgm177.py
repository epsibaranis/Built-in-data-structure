# -*- coding: utf-8 -*-
"""
pgm no 177
Created on Mon Jan 10 16:15:14 2022
covert all the uppercase letter to lowercase in a given text
@author: tt
"""
s1=input('s1=?')
l=len(s1)
s2=''
for i in range(l):
    d=ord(s1[i])
    if d>=65 and d<=90:
        e=d+32
        a=chr(e)
        s2=s2+a
    else:
        b=chr(d)
        s2=s2+b
print(s2)