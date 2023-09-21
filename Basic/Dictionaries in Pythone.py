# Dictionaries is a collection of ordered, changeable data but not allow to duplicate the data
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

student = {
    'name': 'Adil',
    'age': 25,
    'courses': ['Math','Physics']
}

print('Show all the data in a student dictionary: ',student)
print('Show the data of key name in student dictionary: ',student['name'])

student1 = {
    'name': 'Adil',
    'age': 25,
    'courses': ['Math','Physics'],
    'age': 30
}

print('Duplicate values will overwrite existing values:',student1)

#Methods
print('Length of student dictionary: ',len(student1))
print('Type of student dictionary: ', type(student1))
print('Student1 Dictionary keys are:',student1.keys())
print('Student1 Dictionary values are:',student1.values())
print('Student1 Dictionary pairs are:',student1.items())

for key in student1:
    print(key)

#Constructor
thisdict = dict(name = "Adil", age = 23, country = "Pakistan")
print(thisdict)

