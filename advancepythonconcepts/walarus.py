# what is a walarus operator in python?
# The walrus operator (:=) is a new assignment expression introduced in Python 3.8
# It allows you to assign values to variables as part of an expression
# This can help to reduce redundancy and improve code readability in certain situations

def very_slow_function():
    print("Starting a very slow function")
    return 7


if (n := very_slow_function()) > 5:  # here we are using walrus operator to assign the value returned by very_slow_function to n and also check if it is greater than 5
    print(n)

else:
    print("n is less than or equal to 5")
    
# without walrus operator we would have to do it like this
n = very_slow_function()
if n > 5:
    print(n)
else:
    print("n is less than or equal to 5")
    
# another use case is with while loops and input function 
inputs = []
while (current_input := input("Enter something (or 'quit' to stop): ")) != "quit":
    inputs.append(current_input)
print("You entered:", inputs)

# here we are using walrus operator to assign the value returned by input function to current_input and also check if it is not equal to 'quit'

# without walarus operator we would have to do it like this
inputs = []
while True:
    current_input = input("Enter something (or 'quit' to stop): ")
    if current_input == "quit":
        break
    inputs.append(current_input)