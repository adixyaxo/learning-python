class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @property
    def first_name(self):
        l =  self.name.split(" ") # here we are returning first value of the list ie the first name
        # l = self.name.split(" ")[0] This will give you a list 
        return l[0]
    
    @first_name.setter
    def first_name(self,new):
        l = self.name.split(" ")
        self.name = f"{new} {l[1]}"

          
jack = employee("jack halwa",34000)
jack.projects = 6
print(jack.projects) 

# with property and setter now we can do is
print(jack.first_name) 
jack.first_name = "balua"
print(jack.name)