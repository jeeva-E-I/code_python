#CLASS AND OBJECTS

class User:
  pass
class Customer:
  bank_name = 'HDFC Bank' #Class variable
  
  def __init__(self,name,age,initial_amount):
    self.name = name #Instance variable
    self.age = age
    self.balance = initial_amount
  
  def deposit(self,amount): #Local variable (amount)
    self.balance += amount
    print(f'Deposit of ${amount} and the total balance is {self.balance}')

c1 = Customer("John",19,6000) 
c1.deposit(450)
print(c1.bank_name)

user = User() # Object creation
user.id = 1 # Assigning attributes "{id}" is the attribute
user.user_name = "Jeeva"
print(user.user_name)
