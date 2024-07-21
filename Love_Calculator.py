#Love calulator
print("The Love Calculator is calculating your score...")

name1 = input("Enter Your Name:") # What is your name?
name2 = input("Enter Their Name:") # What is their name?

combine_name = name1 + name2
combine_name.lower()

t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
first_digit = t + r + u + e

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
second_digit = l + o + v + e

first_digit = str(first_digit)
second_digit = str(second_digit)
love_score = first_digit + second_digit
love_score = int(love_score)

if (love_score<100) or (love_score>90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  