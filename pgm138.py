# -*- coding: utf-8 -*-
"""
pgm no 138
Created on Sun Jan  9 11:35:19 2022
Number is Even or odd in between two limits
@author: tt
"""
a=int(input('a='))
b=int(input('b='))
for i in range (a+1,b):
    if i%2==0:
     print('Even Number',i)
    else:
     print('Odd Number',i)

