# magic or dunder meathords are nothing but double underscore meathords


class employee:
    company= "HP"
    def __init__(self,name,salary): #init is a dunder meathord to initiate an object it is magic meathord
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return f"The name of the employee is {self.name} and his salary is {self.salary}"

    def __repr__(self): # it is mostly used by developers to debug 
        return f"name : {self.name} \nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)

e1 = employee("harapa",10000)
print(e1.name,e1.salary)

print(str(e1)) # for the user

print(repr(e1)) # for the developer or the debugger

print(len(e1))

# Look in the python handbook for more dunnder or magic meathords