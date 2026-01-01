# tuples are order immutable collection of items
# here immutable means we cannot change the items once defined
# tuples are defined using parentheses ()

my_tuple = (1,2,3,4,5)
print(my_tuple)

# how do you create a tuple with a single item
single_item_tuple = (1,) # note the comma after the item 
print(single_item_tuple)

# accessing items in a tuple
print(my_tuple[0])  # first item
print(my_tuple[-1]) # last item
print(my_tuple[1:4]) # slicing items from index 1 to 3


#tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)
# you can also use asterisk to unpack remaining items
a, *b = my_tuple

# .count() method to count occurrences of an item
print(my_tuple.count(2))  # output: 1

# .index() method to find the index of an item
print(my_tuple.index(3))  # output: 2

# tuples are immutable, so the following operations will raise errors
# my_tuple[0] = 10  # TypeError
# my_tuple.append(6)  # AttributeError
# my_tuple.remove(2)  # AttributeError
# however, you can concatenate tuples to create a new tuple
new_tuple = my_tuple + (6, 7, 8)