#CodeAcademyPythonLesson6.py
#Lesson 6: Functions
#Part 1 Why Functions?
# First user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

# Second user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.")


# Third user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.")


# Fourth user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.")
#Part 2 Defining a Function
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
#Part 3 Calling a Function
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:
directions_to_timesSq()
#Part 4 Whitespace and Execution Flow
print("Checking the weather for you!")
def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
weather_check()
#Part 5 Parameters and Arguments
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")
#Part 6 Multiple Parameters
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total+hotel_total+plane_ticket_price)
calculate_expenses(200, 100, 100, 5)
#Part 7 Types of Arguments
# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in "+first_destination+", then "+second_destination+", and lastly "+final_destination)
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")
#Part 8 Built-in Functions vs User Defined Functions
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price, 1)
print(rounded_price)
#Part 9 Variable Access
# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
#Part 10 Returns
current_budget = 3500.75


def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

shirt_expense = 9
def deduct_expense(budget, expense):
  return budget - expense
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


#Part 11 Multiple Returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third 

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)
#Part 12 Review
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 "+name)
#trip_planner_welcome("Charles")
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(86.75309)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in "+origin)
  print("And you are traveling to "+destination)
  print("You will be traveling by "+mode_of_transport)
  print("It will take approximately "+str(estimated_time)+" hours")

destination_setup("Flavortown", "Disney Land", estimate, "Tricycle")