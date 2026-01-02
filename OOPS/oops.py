# What is object oriented programming?
# Object-oriented programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.
# It is based on several key principles, including encapsulation, inheritance, polymorphism, and abstraction.
# OOP allows for better organization of code, reusability, and easier maintenance.
# In OOP, objects are instances of classes, which define the structure and behavior of the objects.
# Classes are blueprints for creating objects, and they can contain attributes (data) and methods (functions) that operate on that data.

'''
Docstring for OOPS.oops
This module provides an overview of Object-Oriented Programming (OOP) concepts in Python.
In oops we will explore the fundamental principles of OOP, including classes, objects, inheritance, polymorphism, and encapsulation.
The concept of oops is like buildings made with objects (bricks, doors, windows etc.) rather than just functions and logic.
'''
# What is an object?
# An object is an instance of a class that encapsulates data and behavior related to that data
# what is a class?
# A class is a blueprint or template for creating objects, defining their attributes and methods.
# example of object and class in python:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
        
my_car = Car("Toyota", "Camry") #object creation
my_car.display_info()

#here Car is a class and my_car is an object of that class.

# Example of OOP in Python:
 