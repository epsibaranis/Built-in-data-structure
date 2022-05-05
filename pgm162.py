# -*- coding: utf-8 -*-
"""
pgm no 162
Created on Sun Jan  9 19:43:31 2022
Read the string in reverse order
@author: tt
"""
n=input('n=?')
l=len(n)
for i in range(l-1,-1,-1):
    print(n[i],end='')
print()

