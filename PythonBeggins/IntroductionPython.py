# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:19:55 2019

@author: usuario
"""

print("Hello world")

#Variables en python

print("My name is Carlos and I'm 22 years old")

name = "Jonh"
age = "70"
print("My name is " + name + " and I'm " + age + " years old")

character_name = "Tom"
character_age = 50
is_male = True

#Strings in phyton

print("Giraffe\nAcademy")
print("Giraffe\"Academy")
phrase = "Giraffe Academy"
print(phrase + " is cool")

#Convert to lower case upper case and other functions

print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("Aca"))
print(phrase.replace("Giraffe", "Elephant"))


#NUMBERS IN PYTHON

print( 10 % 3)

num = 5
print( str(num) + " is awesome")
print(abs(num))
print(max (4,6))
print(round(3.2))

from math import *
print(sqrt(num))


#Input from users

name = input("Enter your name: ")
print("Hello " + name + "!")
age = input("Enter your age: ")

#Basic calculator in python

num1 = input ("Enter a number: ")
num2 = input ("Enter a number: ")
result = float(num1) + float(num2)
print(result)

#Mad libs game

print("Roses are red")
print("Violets are blue")
print("I love you")

print("Roses are {color}")
print("{plural noun} are blue")
print("I love {celebrity}")

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


#Lists

friends = ["Kevin", "Karen", "Jim"]
print(friends)
print(friends[0])
print(friends[1:])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends)

#Functions with lists

lucky_numbers = [4, 8, 15, 23, 47]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
print(friends.index("Kevin"))
friends.insert(3,"Kevin")
print(friends.count("Kevin"))
lucky_numbers.sort()
print(friends)
friends2 = friends.copy()

#TUPELS

coordinates = (4, 5)
print(coordinates[0])
print(coordinates)
#coordinates[1] = 10


#Functions in Python

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

def say_hi(name, age):
    print("Hello " + name + " your age is " + str(age))

say_hi("Mike", 70)

def cube(num):
    return num*num*num

print(cube(3))
result = cube(3)
print(result)

#Conditions Statments

is_male = True
if is_male:
    print("you are a male")
else:
    print("You're a woman")
    
is_male = True
is_tall = True

if is_male or is_tall:
    print("You're a male or tall or both")
else:
    print("You neither male or tall")
    
    
is_male = True
is_tall = False

if is_male and is_tall:
    print("You're a tall male")
else:
    print("You're either not male or not tall")
    
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and you are not tall")
    
#If statments and comparision
    
def max_num (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
print(max_num(2,47,5))

#Bigger Calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*": 
    print(num1 * num2)
else:
    print("Invalid operator")
    
#Dictionaries
    
monthConversions = {
     "Jan": "January",
     "Feb": "February",
     "Mar": "March",
}

print(monthConversions["Jan"])
print(monthConversions.get("Nuv", "Not a valid value"))

#While loop

i = 1
while i <=10:
    print(i)
    i +=1
    
#Build a basic guessing games
    
secret_word = "giraffe"
guess =""

while guess != secret_word:
    guess = input("Enter guess: ")
    
print("You win!")

secret_word = "giraffe"
guess =""
guess_count = 1
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count<=guess_limit:
        guess = input("Enter guess: ")
        guess_count +=1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("Out of guesses, LOSER!")
else:
    print("You win")
    
# For loop
    
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jennifer", "Bea", "Monica"]

for name in friends:
    print(name)
    
for index in range(len(friends)):
    print(friends[index])
    
#Exponent function
    
def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

#2Dlists and Nested lops

number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]

print(number_grid[0][0])

for row in number_grid:
    for column in row:
        print(column)
        
#Build a translator
        
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"              
        else:
            translation = translation + letter
    return translation

print(translate(input("Escribe una frase: ")))


#Catching errors in Python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid Input")

   
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
    
#Read from external files
    
employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close() #Good practise

#Writing in files

employee_file = open("employees.txt", "a")#Wite at the end of a file
employee_file.write("\nKelly - Costumer Services")
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("employees1.txt", "a")#Wite a new document WARNING!
employee_file.write("Kelly - Costumer Services")
employee_file.close()

#Modules and pips

import phytonAux
print(x)
#Search list of python Modules


#Modules and Clases

from student import Student

student1 = Student("Jim", "Business", 3.1, False)

print(student1)

#Multiple choice Quiz

question_prompts =[
        "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What color are bananas?\n(a) Teal\n(b)Magenta\n(c) Yellow\n\n",
        "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue \n\n",
]
    

from Questionaire import Question

questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)

#Inheritance

from Chef2 import Chef
from ChineseChef2 import ChineseChef

myChef = Chef()
myChineseChef = ChineseChef()
myChef.makeSalad()
myChineseChef.makeSalad()
myChineseChef.makeSpecial()




        




            
