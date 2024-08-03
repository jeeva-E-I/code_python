# Treasure Island 
import art

print(art.logo_3)
print("Welcome to Treasure island.Your mission is to find the treasure.")

way = input("Move left or right").lower()

if (way == "right"):
    print("OOPS, you have fall into a hole.Your game is over")
elif(way == "left"):
    print("You have entered the next stage")
else:
    print("OOPS, you have fall into a hole.Your game is over")

way = input("Explore or wait").lower()

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

door = input("select one door:").lower()

if(door == 'red'):
    print("burned by Fire.. Game over")
elif(door == 'yellow'):
    print("Eaten by beasts... game over")
elif(door == "blue"):
    print("You win the treasure hunt... You are the winner to become a world's richest man")
else:
    print("game over")
