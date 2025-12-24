def sum(a,b):
    # This is a fucntion to make sum
    c = a + b 
    global z
    z=1 # this reffers to global variable which can be accessed now 
    return c
z=3
print(z) # not able to run will give error 
sum(2,3)
print(z)

