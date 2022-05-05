# -*- coding: utf-8 -*-
"""
pgm no 163
Created on Sun Jan  9 19:43:31 2022
Read the string concatenate in reverse order
@author: tt
"""
a=input('a=?')
b=' '
l=len(a)
for i in range(l,0,-1):
    b=b+a[-i]
print(b)

