class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(self):
        print(self.x,self.y)
    def sum(self , p):
        return point(self.x+p.x , self.y+p.y)
    def __add__(self,p):
        return point(self.x+p.x , self.y+p.y)
    
p1 = point(1,2)
p2 = point(3,5)
p3 = p1.sum(p2)
p3.print_point()

# but can we do p4 = p1 + p2 ? Yes there is a way way is to use __add__ function
# this concept of operator overloading allows us to define custom behavior for operators like +, -, *, etc. for our own classes.
p4 = p1 + p2
p4.print_point()
# sum other examples of operator overloading include __sub__ for -, __mul__ for *, __truediv__ for /, and many more.
# By defining these special methods in our classes, we can make our objects behave more like built-in types, enhancing code readability and usability.
