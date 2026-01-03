'''
Decorator is a function which takes a function , creates a new function2 with use of function and returns the new function2
'''
def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I have executed this function")
    return wrapper()


def say_hello():
    print("Hello")

say_hello()
decorator(say_hello)