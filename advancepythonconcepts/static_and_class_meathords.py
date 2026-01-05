class employee:
    company = "hp"#class variable
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    # INSTANCE MEATHORD
    def info(self):
        print(self.name,self.salary)
        
    # STATIC MEATHORD
    @staticmethod # this is used to create a function in a class without inclusion or assosiation of self
    def sum(a,b): 
        return a+b
    
    # CLASS MEATHORD
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = employee("harapa",1200)
e2 = employee("charapra",1300)
print(employee.company)
# print(employee.name) # this will give an error as name is an instance meathord
e1.info()
print(employee.sum(10,11)) #works without help or static meathord func no need
print(e1.sum(10,11)) #works with help of staticmeathord func

print(e1.company)
print(employee.company)
e1.change_company("company changed")
print(e1.company)
print(employee.company)

# we can see that the class meathord has changed the attribute of class or class varible when it did not find it once in the instance variable 