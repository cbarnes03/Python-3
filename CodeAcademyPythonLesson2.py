#Lesson 2 Control Flow
#Part 1) Boolean Expressions, identify which statement is a boolean expression by yes if so, and no if not.
#ExS:My dog is the cutest dog in the world.
example_statement = "No"
#1S:Dogs are mammals.
statement_one = "Yes"
#2S:My dog is named Pavel.
statement_two = "Yes"
#3S:Dogs make the best pets.
statement_three = "No"
#4S:Cats are female dogs.
statement_four = "Yes"

#Part 2) Relational Operators: Equals and Not Equals
#1S: (5 * 2) - 1 == 8 + 1
statement_one = True
#2S: 13 - 6 != (3 * 2) + 1
statement_two = False
#3S: 3 * (2 - 1) == 4 - 1
statement_three = True

#Part 3) Boolean Variables
my_baby_bool = "true"
print(type(my_baby_bool))		#this is a string
my_baby_bool_two = True
print(type(my_baby_bool_two))	#this is a boolean

#Part 4) If Statement
# Enter a user name here, make sure to make it a string
user_name = "Dave"
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

#Part 5) Relational Operators 2
x = 20
y = 20

# Write the first if statement here:

if x == y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:

if credits >= 120:
  print("You have enough credits to graduate!")

#Part 6) Boolean Operators: AND
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
#Part 7)Boolean Operators: Or
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)


statement_two = (9 + 5 <= 15) or (7 != 4 + 3)


credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

#Part 8) Boolean Operators: not
statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate")  
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!") 
#Part 9) Else statement
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")
#Part 10)Else If Statements
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
#Part 11) Review
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  new_weight = weight * 0.91
  print("Your weight will be " + str(new_weight) + " Venus.")
elif planet == 2:
  new_weight = weight * 0.91
  print("Your weight will be " + str(new_weight) + " on Mars.")
elif planet == 3:
  new_weight = weight * 0.91
  print("Your weight will be " + str(new_weight) + " on Jupiter.")
elif planet == 4:
  new_weight = weight * 0.91
  print("Your weight will be " + str(new_weight) + " on Saturn.")
elif planet == 5:
  new_weight = weight * 0.91
  print("Your weight will be " + str(new_weight) + " on Uranus.")
elif planet == 6:
  new_weight == weight * 1.19
  print("Your weight will be " + str(new_weight) + " on Neptune.")
else:
  print("Incomplete Gravitational Archive: Planet Not Found.")
  
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