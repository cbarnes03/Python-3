#Lesson 3 ERRORS

#Part 1) Syntax Errors
# Fortune Cookie Program 🥠 with 3 errors

import random

fortune = random.randint(0, 4)

if fortune == 0
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
eli fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards"
elif fortune == 4:
  print("The fortune you seek is in another cookie")

# Program without errors
# Fortune Cookie Program 🥠

import random

fortune = random.randint(0, 4)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards")
elif fortune == 4:
  print("The fortune you seek is in another cookie")
  
#Part 2 Name Errors

# Who Wants To Be A Millionaire 💰  with 2 Errors

score = 0

option1 = 'Fresca'
option2 = 'V8'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  scor += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")
# Who Wants To Be A Millionaire 💰 without errors

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Fanta'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")
  
#Part 3) Type Errors
# Area Calculator 📏 with one type error

import math

base = 20
height = 30
area = base * height / 2

print("The triangle area is", area)

length = 2
width = 12
area = length * width

print("The rectangle area is" + area )
    
radius = 36
area = math.pi * radius * radius
    
print("The circle area is", area)
# Area Calculator 📏 without errors

import math

base = 20
height = 30
area = base * height / 2

print("The triangle area is", area)

length = 2
width = 12
area = length * width

print("The rectangle area is", area )
    
radius = 36
area = math.pi * radius * radius
    
print("The circle area is", area)
#Part 4) Review
# this program I wrote intentionally contains a Syntax Error/Name Error/Type Error.
import math


height = 30
width = "15 inches" + 12
length = 15
volume = lengh * width * height
print(volume)

if height >= 30
  print(wow you so tall)