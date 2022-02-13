#CodeAcademyPythonLesson5.py
#Lesson 5 Loops
#Part 1)Why Loops?
# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")

#Part 2)For Loops: Introduction
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game) 

for sport in sport_games:
    print(sport)
	
#Part 3)For Loops: Using Range
promise = "I will finish the python loops module!"

for lines in range(5):
    print(promise)
#Part 4)While Loops: Introduction
# # While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count 
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")

# # Your code below: 

countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")
# or the one-line version:
countdown = 10
while countdown >= 0: print(countdown); countdown -= 1
print("We have liftoff!")
#Part 5)While Loops: Lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print("I am learning about " + python_topics[index] + ".")
  index += 1
#Part 6) Loop Control: Break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
  
    
#Part 7) Loop Control: Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i >= 21:
    print(i)
    continue
#Part 8) Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for amount in location:
      scoops_sold += amount
print(scoops_sold)

#Part 9)List Comprehensions: Introduction
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)
#Part 10)List Comprehensions: Conditionals
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)
#Part 11)Review
# Your code below:
single_digits = range(0,10)
squares = []
cubes =[number ** 3 for number in single_digits]
for numbers in single_digits:
  numbersquared = numbers**2
  squares.append(numbersquared)
  print(numbers)
print(squares)
print(cubes)
