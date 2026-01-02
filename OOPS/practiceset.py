class car:
    def drive(self):
        print("The car is moving")

nissan = car()

nissan.drive()

print("\n-----------------------------------\n")

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hey my name is {self.name} and I am {self.age} years old")
        
aditya = person("aditya" , 19)
aditya.intro()


print("\n-----------------------------------\n")


class animal:
    def sound(self):
        print("Some Sound")

class dog(animal):
    def sound(self):
        print("Bark!!")
        
rocky = dog()
rocky.sound()

