class Animal: # Parent class (superclass)
        def __init__(self, name):
                self.name = name
        def speak(self):
                print("Generic animal sound")
                
class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
        def speak(self): # We *override* the speak method (more on this later)
                super().speak() #reffers to the super class speak function
                print("Woof!")
                
class Cat(Animal): # Cat also inherits from Animal
        def speak(self):
                print("Meow!")
                
# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")
# They both have a 'name' attribute (inherited from Animal):

print(my_dog.name) # Output: Rover
print(my_cat.name) # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:

my_dog.speak() # Output: Woof! will also print genertic animal sound due to use of super function
my_cat.speak() # Output: Meow!

