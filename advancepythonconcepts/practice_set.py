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

print("\n---\n")

class book :
    def __init__(self,title,author,length):
        self.title = title
        self.author = author
        self.length = length
        
    def __str__(self):
        return f"{self.title} written by {self.author}"
        
    def __len__(self):
        return self.length
        
b = book("Clean Code","Aditya Dagar",1000)
print(str(b))
print(len(b))

print("\n---\n")
class NegetiveNumberError(Exception):
    pass

try:
    number = int(input("Enter any number ::"))
    divisor = int(input("Enter divisor ::"))
    
    if number < 0 or divisor < 0 :# the raising of the error must be done in a try block 
        raise NegetiveNumberError("Number cannot be negetive")
    
    print(number/divisor)
except ValueError as e:
    print("The input is not a number")
except ZeroDivisionError as e:
    print("You cannot perform division by zero")


print("\n---\n")

# map filter and reduce 

list1 = [1,2,3,4,5,6,7,8,9,10]

cube = map(lambda x : x*x*x ,list1)

print(list(cube))

def evennumbers(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
even = filter(evennumbers,list1)

print(list(even))

from functools import reduce

def multipy(x,y):
    return x*y

print(x := reduce(multipy,list1))

print("\n---\n")

listwords = []
while True:
    if (x:=input("Enter the text you want to print :")) != "quit":
        if len(x) >= 4:
            listwords.append(x)
        print(x)
    else:
        break
print(listwords)
    
print("\n---\n")

def sum_all(*args):
    total = 0
    for items in args:
        total += items
    return total

print(sum_all(10,11,12,13,15,17,19,10))

def print_details(**dt):
    for key,value in dt.items():
        print(f"{key} : {value}")
    
print_details(name="Alice", age=25, city="Delhi")
# Output:
# name: Alice
# age: 25
# city: Delhi
