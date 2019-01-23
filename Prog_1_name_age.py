# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:42:13 2018

@author: UDITA DAWN
"""

#Program1_name_age

name=input('Please enter your name:')

import datetime
year = datetime.date.today().year

age = input('Please enter your age:')
a = 100 - int(age)
c = year + a

print('{} you\'ll be 100 years old in the year {}'.format(name.upper(),c))

#Extra A
copies = input('No. of times you want to print the result:')

print(('{} you\'ll be 100 years old in {}'.format(name,c)) * int(copies))

#Extra B

print(('{} you\'ll be 100 years old in {}\n'.format(name,c)) * int(copies))