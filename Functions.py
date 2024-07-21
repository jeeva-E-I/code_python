#nested function
def multiply(x,y):
    return x*y
def apply(func,x,y):
    return func(x,y)
result = apply(multiply,5,2)
print(result)

#Arbitary arguments

def func(*name):
    for each_name in name:
        print("hello ",each_name)
func("A","B")

#arbitary keyword arguments

def my_func(**detail):
    for key,values in detail.items():
        print(key,values)

my_func(names='a',fullname ='abc',age=45)
    
#lambda function

a= lambda x: x+5
print(a(5))

def power(n):
    return lambda a: a**n
square = power(2)
cube = power(3)
print(square(2))
print(cube(3))  
