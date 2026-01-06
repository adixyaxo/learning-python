def logger(a):
    def wrapper():
        print("function is going to be called :")
        a()
    return wrapper
    
@logger
def say_hello():
    print("Hello")
    
say_hello()

print("\n---\n")

from time import time


def timer(func):
    def wrapper(n):
        t1 = time()
        result = func(n)
        t2 = time()
        print ((t2)-(t1))
        return result
    return wrapper


@timer
def sum(n):
    a = 0
    for i in range(1,n+1):
        a+=i
    return a

print(x := sum(1000000))


print("\n---\n")

class employee:
    def __init__(self,_salary):
        self._salary = _salary
    
    @property
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self,a): # the name of the setter function should be equal to the name of the property funciton when using setters and getters for creating the funcitons into the properties 
        if a < 0 :
            print("Cant set salary as negetive")
        else:
            self._salary = a
        
e = employee(3)
print(e.salary)
e.salary = 4
print(e.salary)

print("\n---\n")

#static and class meathords

class mathulits:
    def __init__(self):
        pass
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a math ulility function")

a = mathulits()
print(a.add(10,11))

# print(a.description()) # this will give you none because you will be creating a function that returns nothing and printing the vaule of nothing so at last it would do nothing but print none so do as follows and directly call the function 

a.description()

# can we test these meathords without creating an object 
# Yes we can yes we can because these functions rely on the class directy and these meathords can be called from the class without creating and object as shown below 

print(mathulits.add(10,11))
mathulits.description()