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