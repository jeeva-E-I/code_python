#SECRET AUCTION PROGRAM
import os
import art
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

print(art.logo_9)
print("Welcome to the Secret auction program")
dict ={}
def input_dict():
    """Get the input for the bidders"""
    name = input("Enter your name:")
    bid = input("What's your bid: $")
    dict[name] = bid # stores the user name and bid value in a dictionary
    x = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if x =='yes':
        clear()
        input_dict() # Recurssively call the function to add another user name and bid value
    return dict
auction_dict = input_dict() # Tigger the function call
print(auction_dict)
value = 0
key = ""

for y,x in auction_dict.items(): # Using for loop check the items in the dict to get the higher value in the auction
    x = int(x)
    if x > value:
        value = x
        key = y
print(f"The winner is {key} with a bid of ${value}")


     
    