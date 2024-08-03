from game_data import data
import random
import art
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

def statement():
    print(f"{art.logo13}")
    print(f"Compare A: {user1["name"]}, a{user1["description"]}, from {user1["country"]}")
    print(art.vs)
    print(f"Against B: {user2["name"]}, a{user2["description"]}, from {user2["country"]}") 
user1 = random.choice(data)
user2 = random.choice(data)
score = 0
check = True

statement()
while check:
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        
        if user1["follower_count"] > user2 ["follower_count"]:
            score += 1
            user1 = random.choice(data)
            user2 = random.choice(data)
            clear()
            statement()
            print(f"You're right! Current score: {score}.\n")
        else:
            check = False
            print(f"Wrong Answer: Your score is {score}")
    elif choice == 'b':
        if user2["follower_count"] > user1 ["follower_count"]:
            score += 1
            user1 = user2
            user2 = random.choice(data)
            clear()
            statement()
            print(f"You're right! Current score: {score}.\n")
        else:
            check = False
            print(f"Wrong Answer: Your score is {score}")
        
        