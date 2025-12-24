#This is for Learning Strings in Python
format_string = "Hello, {}. Welcome to {}!"
name = "Alice"
place = "Wonderland"
formatted = format_string.format(name, place)
print(formatted)  # Output: Hello, Alice. Welcome to Wonderland!

# or we can use f-strings (Python 3.6+)
formatted_fstring = f"Hello, {name}. Welcome to {place}!"
print(formatted_fstring)  # Output: Hello, Alice. Welcome to Wonderland!
# String methods
sample_string = "  Hello, World!  "
print(sample_string.lower())  # Output:   hello, world!
print(sample_string.upper())  # Output:   HELLO, WORLD!
print(sample_string.strip())  # Output: Hello, World!
print(sample_string.replace("World", "Python"))  # Output:   Hello, Python!
print(sample_string.split(","))  # Output: ['  Hello', ' World!  ']
print(sample_string.find("World"))  # Output: 8
print(len(sample_string))  # Output: 17
print(sample_string.startswith("  He"))  # Output: True
print(sample_string.endswith("!  "))  # Output: True    
# Multiline strings
multiline_string = """This is a multiline string.
It can span multiple lines.
"""
