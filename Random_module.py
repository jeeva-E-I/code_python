#Random module
import random # A random module is used to generate random numbers

random_num = random.randint(1,10) # it will generate any random number between 1 to 10  
random_float = random.random()
print(random_num)
print(random_float)
random_range = random.randrange(0,10,2)
print(random_range)
ran_float = random.random() * 10 # it will create random number between 1 to 9.99999 not 10.0
print(ran_float)