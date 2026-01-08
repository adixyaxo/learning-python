import argparse

# look at the documentation for more information of this module

parser = argparse.ArgumentParser(description='simple calculator')

parser.add_argument("num1",type = float, help="first number")
parser.add_argument("num2",type = float, help="second number")

parser.add_argument("operation",choices= ["add","sub","div","mul"], help = "operations to perform" )

args = parser.parse_args()

print(args)

if (args.operation == "add"):
    print(f"{args.num1+args.num2}")
elif (args.operation == "sub"):
    print(f"{args.num1-args.num2}")
elif (args.operation == "div"):
    try:
        print(f"{args.num1/args.num2}")
    except ZeroDivisionError as e :
        print("You cannot divide by zero")
elif (args.operation == "mul"):
    print(f"{args.num1*args.num2}")
else :
    print("wrong choice enter again")