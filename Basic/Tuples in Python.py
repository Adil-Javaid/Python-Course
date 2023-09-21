# Tuples is a collection of ordered but unchangeable.
# Tuples are in ordered, it means that the items have a defines order, and that order will not change
# Tuples are use to store multiple items in a single variable with different data types
# Tuple is a built in data type in python
# It allows duplicate elements

tuple = ("Apple", 100, 'Math',10.5, 100)
print(tuple)

#Create a tuple that have a course and marks of that course
course_marks = (('ICT',60),('OOP',69),('PF',80))
print(course_marks)

#Ordered the tuples
unorderd = (5,4,7,1,3)
print(unorderd)
ordered = sorted(unorderd)
print('',ordered) #Its a list 
print(unorderd[0]) #can not change

#Length of a tuple
print('Length of a tuple course_marks is: ',len(course_marks))
print('Length of a tuple unordered is: ',len(unorderd))

# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
new_tuple = ("apple",)
not_a_tuple = ("apple")
print('Its a tuple',type(new_tuple),new_tuple)
print('Its not a tuple. Its a string',type(not_a_tuple),not_a_tuple)

tuple_types = (100, 'History', "It's a six.", 100, 20.5,False)
print('Tuples have a different data types:',tuple_types)