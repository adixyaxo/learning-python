def logger(a):
    def wrapper():
        print("function is going to be called :")
        a()
    return wrapper
    
@logger
def say_hello():
    print("Hello")
    
say_hello()

print("\n---\n")

from time import time


def timer(func):
    def wrapper(n):
        t1 = time()
        result = func(n)
        t2 = time()
        print ((t2)-(t1))
        return result
    return wrapper


@timer
def sum(n):
    a = 0
    for i in range(1,n+1):
        a+=i
    return a

print(x := sum(1000000))
