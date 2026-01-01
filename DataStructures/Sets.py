# SETS is a collection of well defined unique items where elements are unordered and unindexed and cannot be repeated

set = {1,2,3,4,5,5,4,3,2,1} # duplicate items will be ignored
print(set) # output: {1, 2, 3, 4, 5}
print(type(set)) # output: <class 'set'>

# set meathods
set.add(6) # add item to the set
print(set)
set.remove(3) # remove specific item it is an error if item not found
print(set)
set.discard(10) # remove specific item, no error if item not found
print(set)
set.pop() # remove and return an arbitrary item means it will remove any random item
print(set)
set.clear() # remove all items from the set
print(set)

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# set operations
print(a.union(b)) # combine two sets
print(a.intersection(b)) # common items in both sets
print(a.difference(b)) # items in a but not in b
print(b.difference(a)) # items in b but not in a
print(a.symmetric_difference(b)) # items in either a or b but not in both
print(a.isdisjoint(b)) # check if two sets have no items in common
print(a.issubset(b)) # check if a is subset of b
print(a.issuperset(b)) # check if a is superset of b



# set comprehension
squared_set = {i**2 for i in range(10)}
print(squared_set)
