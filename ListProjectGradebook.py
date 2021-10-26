last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects =["phsyics", "calculus", "poetry", "history"]									# list that contains the subjects 
grades = [98, 97, 85, 88]																# list that contains the grades
gradebook = [["phsyics", 98], ["calculus", 97],["poetry", 85],["history", 88]]			# 2D list that contains both
gradebook.append(["computer science", 100])												# adds new subject & grade to 2D list
gradebook.append(["visual arts", 93])													# adds new subject & grade to 2D list
gradebook[-1][-1] += 5																	# changes grade for visual arts 
gradebook[2].remove(85)																	# removes grade from poetry in 2D list
gradebook[2].append("Pass")																# adds "Pass" in place of grade for poetry
full_gradebook = last_semester_gradebook + gradebook									# makes new list containing both the gradebook I made & the last_semester_gradebook
print(full_gradebook)																	# prints
