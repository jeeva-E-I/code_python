# Number Guessing Game
import os
import random
import art

print(art.logo_12)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a Number between 1 to 100")
comp_num= random.randint(1,100)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
   
def valid():
    type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if type == 'easy':
        chance = 10
        guess(chance)
    else:
        chance = 5
        guess(chance)
        
def guess(value):    
    print(f"You have {value} attempts remaining to guess the number.")
    if value == 0:
        print("____________________GAME OVER____________________")
        check = input("Do you want to play again. type 'yes' for new game, type 'no' to exit: ").lower()
        if check == 'yes':
            clear()
            global comp_num
            comp_num = random.randint(1,100)
            valid()
        else:
            return
            
    guess_num = int(input("Make a guess: "))
    if guess_num == comp_num:
        print("You won")
    elif guess_num < comp_num:
        print("Too low")
        value -= 1
        guess(value)
    else: 
        print("Too High")
        value -= 1
        guess(value)    


valid()
