#Function example
def wishes(): # function definiton 
    print("Hello everyone") 
    print("function definition")
    print("Example")

# wishes()# function call 

# #function with return values
# def format_name(name):
#     if name == "":
#         return "Invalid input"
#     formated_name = name.title()
#     return f"The formated name : {formated_name}"
# print(format_name("jeeva"))

# nested function
# def multiply(x,y):  #positional argument
#     return x*y
# def apply(func,x,y):
#     return func(x,y) 
# result = apply(multiply,5,2)
# print(result)

# #Arbitary arguments

# def func(*name):
#     for each_name in name:
#         print("hello ",each_name)
# func("A","B","jeeva",1234)

# #arbitary keyword arguments
 
# def my_func(**detail):
#     print(detail)
#     for key,values in detail.items():
#         print(key,values)

# my_func(names='a',fullname ='abc',age=45)
    
# #lambda function
# a= lambda x: x+5
# print(a(5))

# def power(n):
#     return lambda a: a**n
# square = power(2) 
# cube = power(3) 
# print(square(6))
# print(cube(3))  
