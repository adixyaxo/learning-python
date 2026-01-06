# map filter and reduce are higher order functions in python
# they operate on iterables like lists, tuples, etc. 
# they provide a concise and functional way to process data and perform common operations on sequences of data without using explicit loops.


numbers = [1, 2, 3, 4, 5, 6 , 21, 45]
def square(x):
    return x*x

new = map(square, numbers) # map applies the function to each item in the iterable
# this returns a map object which we would have to type cast or convert to list or tuple to see the result
print(list(new)) # converting map object to list to see the result