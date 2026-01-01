import math
import mymodule
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120
print(math.pow(2, 3))  # Output: 8.0
print(math.gcd(48, 18))  # Output: 6
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))  # Output: 1.0
print(math.log(100, 10))  # Output: 2.0
print(math.exp(2))  # Output: e^2 ≈ 7.389
print(math.ceil(4.3))
print(math.floor(4.7))
print(math.radians(180))
print(math.degrees(math.pi))
print(math.isqrt(20))
print(math.comb(5, 2))
print(math.perm(5, 2))


# there are more built in modules in python like os, sys, datetime, random, json, re, subprocess, threading etc. which you can explore in the documentation. https://docs.python.org/3/library/
# https://docs.python.org/3/py-modindex.html

# importing custom module
print(mymodule.greet("Alice"))  # Output: Hello, Alice!

#  external modules can be installed using pip install requests
import requests
response = requests.get('https://google.com')
print(response.status_code)  # Output: 200