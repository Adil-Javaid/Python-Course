# Sets is a collection of unordered and unchangeable, and unindexed data.
# We can add and remove elements in sets.
# Sets are written with curly brackets
# No duplicate elements allowed in sets
# Set items can be of any data type

course_Marks_Set = {"ICT",100,"OOP",50}
print(course_Marks_Set)

# print(course_Marks_Set[0]) 'set' object is not subscriptable

#duplicate elements
courses = {'Art', "Urdu", 'Math','Urdu'}
print(courses)

sets_type = {"apple", "banana", "cherry", True,False, 1, 2}
print(sets_type) #true and 1 both are same so that's why 1 is not printed

print(len(sets_type))

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)