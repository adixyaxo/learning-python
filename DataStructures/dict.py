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

