# Dictionary in Python 
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.

marks = {
    "Aditya": 85,
    "Rahul": 92,
    "Priya": 78,
    "Karan": 95
}

print(marks)  # Print the entire dictionary
print(type(marks))  # Output: <class 'dict'>

# The key that you are using should be hashable (immutable) types like strings, numbers, or tuples can be used as keys
# whereas lists or other dictionaries cannot be used as keys.

# Accessing values using keys
print(marks["Aditya"])  # Output: 85
print(marks.get("Priya"))  # Output: 78
# Using get() method to avoid KeyError
print(marks.get("Ankit"))  # Output: Not Found
# Adding or updating key-value pairs
marks["Ankit"] = 88  # Adding a new key-value pair
marks["Rahul"] = 95  # Updating an existing key's value
print(marks)

"--------------------------------"

# Dictionary methods
marks.keys()  # Returns a view object of all keys
marks.values()  # Returns a view object of all values
marks.items()  # Returns a view object of key-value pairs
marks.pop("Karan")  # Removes the key-value pair with the specified key
print(marks)
marks.clear()  # Removes all key-value pairs from the dictionary
print(marks)


"--------------------------------"
# How to print dictionary in a formatted way or pretty way or in a table way
import pprint
marks = {
    "Aditya": 85,
    "Rahul": 92,
    "Priya": 78,
    "Karan": 95
}
pprint.pprint(marks)
pprint.pprint(marks, width=1)  # print each key-value pair in a new line
"--------------------------------"


# Dictionary comprehension

# dict of numbers and table of 5
table_of_5 = {i: i*5 for i in range(1, 11)}
print(table_of_5)