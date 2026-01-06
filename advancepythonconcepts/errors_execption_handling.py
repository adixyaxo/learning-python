def add (): #if only there is a function we can return value in the execption block otherwise no return only print
    while True:
        try:    
            a = int(input("Enter the first number  ::  "))
            b = int(input("Enter the second number  ::  "))

            def sum(x,y):
                return x+y

            print(sum(a,b))
        except ValueError as e:
            print("Value error ocured")
            return e
        
        except Exception as e: #This will include all the errors
            print("Some error occured",e)
            return None
        
        else : #executes when there is no error present
            print("There was no error")
            
        finally: #executes always no matter what
            print("These peice or block of code always executes no matter what")
            
        if a==0 & b==0:
            raise ValueError ("Dont waste the time adding to zeros") #this is made to raise an error and crash a programme on purpose
        
#IMPORTANT IMPORTANT IMPORTANT 
# for creating custom errors we do this 
class NegetiveNumberError(Exception):
    pass

# after doing this we have sucessfully created a new error called NegetiveNumberError