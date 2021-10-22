#Magic8Ball
import random


name = "Charlie"
question = "Will I get hired?"
answer = ""
if name == " ":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
elif question == " ":
  print("To know the answer, one must know the question.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
random_number = random.randint(1,11)
#print(random_number)
if random_number == 1:
  answer = "Yes - definitely."
  print(answer)
elif random_number == 2:
  answer = "It is decidedly so."
  print(answer)
elif random_number == 3:
  answer = "Without a doubt."
  print(answer)
elif random_number == 4:
  answer = "Reply hazy, try again."
  print(answer)
elif random_number == 5:
  answer = "Ask again later."
  print(answer)
elif random_number == 6:
  answer = "Better not tell you now."
  print(answer)
elif random_number == 7:
  answer = "My sources say no."
  print(answer)
elif random_number == 8:
  answer = "Outlook not so good."
  print(answer)
elif random_number == 9:
  answer = "Very doubtful."
  print(answer)
elif random_number == 10:
  answer = "It is quite unlikely."
  print(answer)
elif random_number == 11:
  answer = "Absolutely not."
  print(answer)
else:
  print("Error")
