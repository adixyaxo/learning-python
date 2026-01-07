# in python we can read a file write to a file and can also append in a file

# IMPORTANT NOTE DO cd ./folder_name or name sure you are in right directry in terminal with the files to run this programme 
# cd .\Fileio\

a_file = open("aditya.txt","r") # if we want to read txt files we write rt and if we want to read binary files we write rb

content = a_file.read()

print(content)

a_file.close()
