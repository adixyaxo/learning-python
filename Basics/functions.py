

def avergae(a,b,c,d=0):
    # This function calculates the average of four numbers
    # here the default value of d is 0 which can be changed or overridden while calling the function
    return (a + b + c + d) / 4
print(avergae(2,4,6,7))

# lambda function
square = lambda x: x * x
sum = lambda a, b: a + b
print(square(5))  # Output: 25
print(sum(3, 7))  # Output: 10

# why do we use lambda functions?
# Lambda functions are used for creating small, anonymous functions at runtime.
# They are often used in situations where a simple function is needed for a short period of time,
# such as in higher-order functions like map(), filter(), and reduce().It preserves the formatting,
# including line breaks and indentation.

# recursion
def factorial(n):
    # This function calculates the factorial of a number using recursion
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120

def fibonacci(n):
    # This function returns the nth Fibonacci number using recursion
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(7))  # Output: 13 
# Note: Recursive functions can be less efficient for large inputs due to repeated calculations.
# you must have a base case to prevent infinite recursion.

