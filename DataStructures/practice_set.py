fruits = [ "apple", "banana","cherry"]

fruits[1]="orange"
print(fruits)

print(len(fruits))

print("-------------------------")

no_1to10 = [ i for  i in range(1,10)]
print(no_1to10)
print(no_1to10[:3])
print(no_1to10[-3:])

print("-------------------------")

numbers = [5, 2, 9, 1, 7]
numbers.sort()
numbers.append(10)
numbers.remove(2)


print("-------------------------")



names = ["Alice", "Bob", "Charlie"]
names.insert(1,"David")
print(names)



print("-------------------------")



coordinates = (10, 20)
print(coordinates)

# coordinates[0]=50  gives traceback error TypeError: 'tuple' object does not support item assignment

list_coordinates = [coordinates[0],coordinates[1]]
list_coordinates[0]=50
print(list_coordinates)
tuple_changed_coordinates = (list_coordinates[0],list_coordinates[1])

print(type(tuple_changed_coordinates))
print(tuple_changed_coordinates)


print("-------------------------")



my_set = {1, 2, 3, 3, 4}
print(my_set)
# duplicate 3 will get isolated or singled out

my_set.add(5)
my_set.discard(5)
four = {4}  
print(my_set.issuperset(four))
if 4 in my_set : print("yes")


a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))



print("-------------------------")




student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
student["grade"]="A+"
student["city"]="Delhi"

print(student.keys())
print(student.values())
print(student.items())