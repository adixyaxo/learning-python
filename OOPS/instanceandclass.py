#instance attributes are specific to an instance and class attributes are specific to a class 

class employee:
    company = "aency" #CLASS ATTRIBUTE
    
    def __init__(self,name,salary,bond,company): # this is a contructor which will take some parameters and intitialise our object with those parameters
        
        self.salary = salary #create an instance attribute of name salary and assign it with salary 
        self.name = name
        self.bond = bond 
        self.company = company #INSTANCE ATTRIBUTE
        pass
    
    def getinfo(self): # this is a meathord
        print(f"The name of the employee is {self.name} and his salary is {self.salary} and he is bonded with company for {self.bond} years")
    
    
    def get_salary(self): # this is a meathord
        return self.salary
    

e1 = employee("aditya",10000,4,"aency_changed")
print(e1.company) # will always print an instance attribute if present

print(employee.company) # this will always print the class attribute 


print(dir(e1)) # dir gets you all the instances and meathords an object as 