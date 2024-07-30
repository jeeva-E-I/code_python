#SECRET AUCTION PROGRAM
import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret auction program")
dict ={}
def input_dict():
    name = input("Enter your name:")
    bid = input("What's your bid: $")
    dict[name] = bid
    x = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if x =='yes':
        clear()
        input_dict()
    return dict
auction_dict = input_dict()
print(auction_dict)
value = 0
key = ""

for y,x in auction_dict.items():
    x = int(x)
    if x > value:
        value = x
        key = y
print(f"The winner is {key} with a bid of ${value}")


     
    