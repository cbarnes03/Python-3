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