# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:47:48 2019

@author: Carlos Cabrera
"""

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

#The input returns a string
max = input("maximum value of Fibonacci serie: (greater than 1) ")
max = int(max)

#We have to know that the Fibonacci is: 1,1,2,3,5,8,13,21,34...
def function(max):
    num1 = 1
    num2 = 1
    sum = 1
    while num2 <= max:
        sum = sum + num2
        aux = num2 #it is necessary because we want change two values that depends each other at the same time
        num2 = num1 + num2
        num1 = aux
    return sum

print('The result is: ' + str(function(max)))
    
    
    
