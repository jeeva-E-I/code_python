#ROCK PAPER SCISSORS PROGRAM
import random as rd
import art
print(art.logo_4)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_input = rd.randint(0,2)
print("YOUR CHOICE")
if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
else:
  print(scissors) 

print("COMPUTER CHOICE")
if computer_input == 0:
  print(rock)
elif computer_input == 1:
  print(paper)
else:
  print(scissors) 

if user_input == computer_input:
  print("The game end in Draw")
elif user_input == 0:
  if computer_input == 2:
    print("You won")
  else:
    print("You lose")
elif user_input == 1:
  if computer_input ==0:
    print("You Won")
  else:
    print("You Lose")
else:
  if user_input == 2 and computer_input == 1:
    print("You Won")
  else:
    print("You Lose")