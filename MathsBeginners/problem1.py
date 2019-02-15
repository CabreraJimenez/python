# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:06:31 2019

@author: Carlos Cabrera
"""

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
#We are going to resolve this problems for any number:
number = input('Find the sum of all the multiples of 3 or 5 below: ' )
number = int(number)

#The rest is the best option 
def function(num):
    i=1
    sum=0
    while i < number:
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
        i += 1
    return sum

print( 'The sum of all the multiples of 3 or 5 below ' + str(number) + ' is ' + str(function(number)))
        
        
