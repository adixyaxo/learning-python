# map filter and reduce are higher order functions in python
# they operate on iterables like lists, tuples, etc. 
# they provide a concise and functional way to process data and perform common operations on sequences of data without using explicit loops.

def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
    
number = [1, 2, 3, 4, 5, 6 , 21, 45]

new = filter(is_greater_than_9, number) # filter applies the function to each item in the iterable and returns only those items for which the function returns True

print(list(new)) # converting filter object to list to see the result

lambda_new = filter(lambda x: x > 9, number) # using lambda function to achieve the same result
print(list(lambda_new))
