#Random module
import random # A random module is used to generate random numbers

random_num = random.randint(0,1) # it will generate any random number between 1 to 10  
random_float = random.random() # it will create random number between 1 to 4.9 not 5
print(random_num)

# heads or tails program
import random
value = random.randint(0,1)
if(value == 1):
  print("Heads")
else:
  print("Tails")