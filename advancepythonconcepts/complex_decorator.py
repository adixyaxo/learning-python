def say_hello():
    print("Hello")
    
def say_yellow(a):
    def decorator():
            def wrapper():
                print("Yellow")
                a()
            return wrapper()
    return decorator()

say_yellow(say_hello)
