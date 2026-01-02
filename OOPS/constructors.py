# we use construtors in python to initialise our object 

class employee:

    def __init__(self,name,salary,bond): # this is a contructor which will take some parameters and intitialise our object with those parameters
        
        self.salary = salary #create an instance attribute of name salary and assign it with salary 
        self.name = name
        self.bond = bond 
        pass
    
    def getinfo(self): # this is a meathord
        print(f"The name of the employee is {self.name} and his salary is {self.salary} and he is bonded with company for {self.bond} years")
    
    
    def get_salary(self): # this is a meathord
        return self.salary
    


e1 = employee("aditya",10000,4)
print(e1.name)
print(e1.get_salary())
e1.getinfo()