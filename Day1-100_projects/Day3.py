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
