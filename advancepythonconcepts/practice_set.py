def logger(func):
    print("function is going to be called :")
    func()
    
@logger
def say_hello():
    print("Hello")