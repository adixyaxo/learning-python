# f = open("linebyline", "r")
# content = f.read()
# print(content)
# f.close()

# BETTER APPROACH IS BELOW 

with open("linebyline" , "r") as f:
    content = f.read()
    print(content)
    
    # there is no need to close the file in with the file is automatically closed when using with syntax
    # WITH IS A CONTENT MANAGER 
    # EVEN WHEN AN ERROR OCCURS THE FILE IS AUTOMATICALLY CLOSED 
    # BUT WE DO NEED TO CHECK FOR ERRORS TO STOP FILE FROM CRASHING INITIALLY 