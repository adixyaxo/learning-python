# this fucntion deals with decorators with arguments 

def repeat(n): #repeat is decorator 
    def decorator(func): #func is function ie say_hello
        def wrapper(a): # a is argument ie "aditya"
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(10)
def say_hello(a):
    print(f"Hello {a}")
    
say_hello("aditya")