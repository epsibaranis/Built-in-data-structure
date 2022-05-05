# -*- coding: utf-8 -*-
"""
pgm no 164
Created on Sun Jan  9 19:43:31 2022
Read the string and it is polyndrome or not
@author: tt
"""
a=input('a=?')
b=''
l=len(a)
for i in range(l,0,-1):
    b=b+a[-i]
if b==a:
    print('String is Polyndrome')
else:
    print('The string is not Ployndrome')
