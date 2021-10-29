#CodeAcademyPythonLesson4.py 
# Working with Lists
#Part 1) Adding by Index: Insert
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)
#Part 2) Removing by Index: Pop
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

#Part 3)Consecutive Lists: Range
# Your code below: 

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

#Part 4)The Power of Range!
# Your code below: 

range_five_three = range(5, 15, 3)
range_diff_five = range(0,40,5)

print(list(range_five_three))
print(list(range_diff_five))

#Part 5) Length
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list1 = range(2, 3000, 10)
range_list2 = range(2, 3000, 100)
# Your code below: 

long_list_len = len(long_list)
print(long_list_len)
range_list1_length = len(range_list1)
print(range_list1_length)
range_list2_length = len(range_list2)
print(range_list2_length)

#Part 6) Slicing Lists I
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
middle = suitcase[2:4]
beginning = suitcase[0:2]

# Your code below: 
print(beginning)
middle = suitcase[2:4]
print(middle)

#Part 7) Slicing Lists II
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

#Part 8) Counting in a List
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

#Part 9) Sorting Lists I
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
print(cities)
#Part 10) Sorting Lists II
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

#Part 11) Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[1]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory = sorted(inventory)
print(inventory)

# INTRODUCTION TO zip()
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
