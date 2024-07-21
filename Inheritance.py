#INHERITANCE
class A:
    def a(self):
        print("I'm A parent classs ")
class B(A):
    def b(self):
        print("Im B inherited class") #single level inheritance
obj = B()
print(obj.a)
print(obj.b)

class C(B):
    def c(self):
        print("Im c inherited from B class") # Multi level inherritance
obj2 = C()
print(obj2.a)
print(obj2.b)
print(obj2.c)

#Inheriting constructor in class
class Parent:
    def __init__(self,sname,sage):
        self.sname =sname
        self.sage = sage
class Child:
    def __init__(self,sname,sage,school):
        Parent.__init__(self,sname,sage)
        self.school = school
#we can use super() method by adding super() in the place of parent and the self can be removed
obj3 = Child("John",16,'ABC')
print(obj3.sname)
print(obj3.school)
print(obj3.sage)

