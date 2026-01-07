''' IN THIS PROGRAMME WE WILL UNDERSTAND HOW TO READ THE FILES LINE BY LINE '''
try:
    f = open("linebyline", "r")
    for line in f:
        print(line)
    f.close()
except Exception as e :
    print(e)