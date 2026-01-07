# in python we can read a file write to a file and can also append in a file

# IMPORTANT NOTE DO cd ./folder_name or name sure you are in right directry in terminal with the files to run this programme 
# cd .\Fileio\

a_file = open("aditya.txt","r") # if we want to read txt files we write rt and if we want to read binary files we write rb

content = a_file.read()

print(content)

a_file.close()

# for writing do following 

jhon_doe = open("jhon_doe","w")

string_ = '''This is a multi line string which i am going to write in jhon_doe.txt 
Hi i am jhon the don
hahahahhahah
'''

jhon_doe.write(string_)

jhon_doe.close()