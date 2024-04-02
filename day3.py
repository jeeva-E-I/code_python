#odd or even 

number = int(input("enter the value:"))
if(number%2 == 0):
    print("the number is even number",number)
else:
    print("the number is odd number",number)
    
#BMI calculation

height = float(input("Enter the height:"))
weight = int(input("Enter the weight:"))
result = weight / (height ** 2)
result = int(result)
print(result)

#Leap year
year = int(input("enter the year:"))
if (year %400 == 0) and (year %100 ==0):
    print("leap year")
elif (year %4 ==0) and (year %100 !=0):
    print("leap year")
else:
    print("Not a leap year")

#pizza order pratice

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
if size == 'S':
  bill = 15
  if add_pepperoni== 'Y':
    bill += 2
  if extra_cheese == 'Y':
    bill += 1
elif size =='M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
else:
  bill = 25
  if add_pepperoni == "Y":
    bill +=3
  if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}.")
    
 #Love calulator
print("The Love Calculator is calculating your score...")

name1 = input() # What is your name?
name2 = input() # What is their name?

combine_name = name1 + name2
lower_case = combine_name.lower()

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

if (love_score<10) or (love_score>90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  
# Treasure Island 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure island.Your mission is to find the treasure.")
way = input("Move left or right")
way.lower()
if (way == "right"):
    print("OOPS, you have fall into a hole.Your game is over")

elif(way == "left"):
    print("You have entered the next stage")
else:
    print("OOPS, you have fall into a hole.Your game is over")
way = input("Explore or wait")
way.lower()
if(way =="explore"):
    print("You are attacked by Trout... You are dead.... Game is over")
elif (way == 'wait'):
    print("magical door has been opened... Qualified to next stage")
else:
    print("You stucked in the maze...Game is over")
print("three doors are availabe enter one door to win the treasure hunt")
print("red")
print("blue")
print("yellow")
door = input("select one door:")
door.lower()
if(door == 'red'):
    print("burned by Fire.. Game over")
elif(door == 'yellow'):
    print("Eaten by beasts... game over")
elif(door == "blue"):
    print("You win the treasure hunt... You are the winner to become a world's richest man")
else:
    print("game over")
