#decorator function  
def my_decorator(func):
    def wrapper():          #wrapper function should return wrapper at the end of the function
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorator
def hello():
    print("hello")
hello()

#generator function
def gen():
    ''' Generator function'''
    yield 1
    yield 2
    yield 3
print(next(gen())) #To Print single value in a generator we need to use Next
for a in gen():
    print(a)
    print(a," is a number")
    print("=============")
