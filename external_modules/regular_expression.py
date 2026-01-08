import re 

#regular expression is a very vast concept which is usually used for pattern searching 

# visit https://regexr.com/ for more 


text = "Hi my name is aditya i want to kill each and everyone i meet Aditya ADITYA"

aditya = re.search("aditya",text)

if aditya:
    print("MATCH FOUND")
    print("Start Index :", aditya.start())
    print("Ending Index :", aditya.end())
    
aditya_all = re.findall("aditya",text,re.IGNORECASE) # case insensitive search

print(aditya_all)

next_text = re.sub("name","naam",text)

print(next_text)