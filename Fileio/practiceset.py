
with open("notes.txt" , "w") as notes:
    notes.write("Learning Python is fun!")
    
with open("notes.txt" , "r") as notes:
    print(notes.read())
    
    
print("\n---\n")

with open("tasks.txt" , "w") as tasks:
    three_lines = '''This is the first line 
Second line is this the
Third is line the this
    '''
    tasks.write(three_lines)
    
with open("tasks.txt" , "a") as tasks:
    tasks.write("Tasks Completed") 
    
with open("tasks.txt" , "r") as tasks:
    line_list = []
    for line in tasks.readlines():
        line_list.append(line)
    print(line_list)
    
    
print("\n---\n")

import os


print(os.getcwd())
 
print(os.listdir())

# os.mkdir("My Folder")

print("\n---\n")

import shutil

shutil.copy("aditya.txt" , "./dir/adityacopy.txt")