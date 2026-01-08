# in python we can read a file write to a file and can also append in a file

# IMPORTANT NOTE DO cd ./folder_name or name sure you are in right directry in terminal with the files to run this programme 
# cd .\Fileio\

a_file = open("aditya.txt","r") # if we want to read txt files we write rt and if we want to read binary files we write rb

content = a_file.read()
# for reading line by line one line at once we use 
line1 = a_file.readline()

# for reading line by line all lines at once we use
lines = a_file.readlines()

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

# for appending data 

jhon_doe = open("jhon_doe","a")
# for both writing and appending we use write function there is no append function in the fileio so for appending open file as a and write and for writing open file as w and write and for reading open file as r and read 
jhon_doe.write('''I am apending this data to jhon doe file lets see the results 
of 
appending
the 
data
''')

# IN CASE OF READ MODE ALWAYS OPEN FILES IN TRY EXCEPT BLOCK TO BY PASS ANY ERROR FOR THE FILE NOT EXITING IN THE DIRECTRY 
# IN CASE OF WRITE AND APPEND MODE THE PROGRAMME AUTOMATICALLY CREATES NEW FILES 

