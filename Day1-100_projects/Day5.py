#Password Generator Project
import random
import art
print(art.logo_5)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]

for i in range(1,nr_letters+1):         # this for loop finds random letters in the list with the range specified by the user
    password.append(random.choice(letters))
    
for i in range(1, nr_numbers+1 ):       # this for loop finds random numbers in the list with the range specified by the user
    password.append(random.choice(numbers))
    
for i in range(1, nr_symbols+1):        # this for loop finds random symbols  in the list with the range specified by the user
    password.append(random.choice(symbols))
    
    
total_length = len(password)
final_password=""

for i in range(0, total_length):        # this loop converts the list of elements into a single string as a final generated password
    word = random.choice(password)
    final_password += word    
print(final_password)