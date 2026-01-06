from functools import reduce # we need to import reduce from functools module
# map filter and reduce are higher order functions in python
# they operate on iterables like lists, tuples, etc. 
# they provide a concise and functional way to process data and perform common operations on sequences of data without using explicit loops.

numbers = [1, 2, 3, 4, 5, 6 , 21, 45]

def sum(a,b):
    return a+b

c = reduce(sum, numbers) # reduce applies the function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.
print(c) # this will add all the numbers in the list and return a single value 
# the process is like (((((1+2)+3)+4)+5)+6)+21)+45)
# numbers = [1, 2, 3, 4]
# step 1: 1+2 = 3
# numbers = [3, 3, 4]
# step 2: 3+3 = 6
# numbers = [6, 4]
# step 3: 6+4 = 10
# final result = 10
