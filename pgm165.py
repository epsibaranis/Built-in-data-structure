# -*- coding: utf-8 -*-
"""
pgm no 165
Created on Sun Jan  9 19:43:31 2022
Read the integer no and it is polyndrome or not
@author: tt
"""
a=int(input('a=?'))
c=str(a)
b=''
l=len(c)
for i in range(l,0,-1):
    b=b+c[-i]
if b==c:
    print('integer is Polyndrome')
else:
    print('The integer is not Ployndrome')
