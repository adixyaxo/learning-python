marks =[1,5,4,6,3,2,7,9,8,0]
#ordered mutable collection of items

print(marks)
print(marks[2:4]) #slicing of lists     


# list meathords
marks.append(600) #add item at the END
marks.insert(2,450) #add item at specific index ##IMPORTANT
marks.remove(1) #remove specific item
marks.pop() #remove last item
marks.sort() #sort the list
marks.reverse() #reverse the list
print(marks)

# list comprehension
squared_marks = [i**2 for i in range (10)]
cube_marks = [i**3 for i in range (10)]
cube_marks_2 = [i**3 for i in range (0,10)]
print(squared_marks)
print(cube_marks)
print(cube_marks_2)