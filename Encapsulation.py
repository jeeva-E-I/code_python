#ENCAPSULATION
class Car:
    __car_price = 250000 #To encapsulate the variable we need to use double underscore 
    def display(self):
        print(self.__car_price)
    
value = Car()
value.display()
