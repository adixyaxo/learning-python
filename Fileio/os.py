import os

# YOUR CAN GO TO THE DOCUMENTATION OF OS MODULE TO LEARN ABOUT MORE FUNCTIONS IN THIS MODULE 

a = os.listdir(".")
print(a)

print(os.getcwd()) # to get the current working directory

print(os.path.exists("jhon_doe")) # to find out if a file exits or not on the specified path 

os.remove() # used to delete a file but not a directory 
os.rmdir() # used to remove only empty directories 