# fibonacci using generator function
def fibo(limit):
    '''Print the fibonacci number of required limit'''
    a,b=0,1
    while a < limit:
        yield a
        a,b = b,a+b
x = int(input("Enter the limit"))
for num in fibo(x):
    print(num)