# we will study about args and kwargs in python

def sum(a,b):
    return a+b

print(sum(342,2)) # normal way of passing arguments to a function
# but what if we have to pass multiple arguments to a function
# we can use *args and **kwargs to pass multiple arguments to a function

def sum_args(*args): # args is a tuple of arguments
    total = 0 # initializing total to 0
    for items in args:
        #args is a tuple so we can iterate through it which contains all the arguments passed to the function
        total += items
    return total

print(sum_args(1,2,3,4,5,6,7,8,9,10)) # passing multiple arguments to the function


def marks(**kwargs): # kwargs is a dictionary of keyword arguments
    for key, value in kwargs.items():
        print(f"The marks of {key} are {value}")
        
marks(math=90, science=85, english=88 , hindi=92) # passing multiple keyword arguments to the function