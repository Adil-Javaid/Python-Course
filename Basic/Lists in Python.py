# List is a collection of ordered and changeable elements. It allows duplicate elements
# List are in ordered, it means that the items have a defines order, and that order will not change
#The list is changeable, meaning that we can change, add, and remove elements in a list
#It allows duplicate elements
#It can store different data types

course_marks = ['History',100,False]
print(course_marks)

courses = ['History', 'Urdu', 'Math']
print('length of the list courses is: ',len(courses))
print('List courses index 0 is: ',courses[0])
print('Negative value of index show the last element in the list: ', courses[-1])

#print('list index out of range error', courses[3])

print('Start from 0th index to 1st index: ',courses[:2])
print('Start from 1st index to last index: ',courses[1:])

#Add element in the last of the list
courses.append('Art')
print(courses)

#Insert by index
courses.insert(2,'Chemistry')
print(courses)

#Insert the list in other list
courses2 = ['ICT','OOP']
courses.insert(2,courses2)
print(courses)

#Extend the courses list
courses1 = ['History', 'Urdu', 'Math']
courses1.extend(courses2)
print(courses1)

#Remove the element in the courses list
courses.remove('History')
print(courses)

#Pop up the last element in the list
print('Pop up the last element in the courses list is: ',courses.pop())
print(courses)

#Reverse the list
courses.reverse() 
print('Reverse the course list: ',courses)

#Sorted by alphabetic or numerically
marks = [100, 90,150, 60, 30, 10]
marks.sort()
print('Sorted the marks list: ',marks)
marks.sort(reverse=True)
print('Sorted the marks list in decending order: ',marks)

#Maximum, Minimum, and Sum
print('Minimum value in the list is: ',min(marks))
print('Maximum value in the list is: ',max(marks))
print('Sum-up the values in the list is: ',sum(marks))

#Index, element exist or not
print('Find the index by putting the element: ',marks.index(90))
print('Element exist in the list printed True else false:', 200 in marks)
print('Element exist in the list printed True else false:', 100 in marks)

print('print in the vertical form: ')
for item in marks:
    print(item)

print('Show with the index:')
for index, marks in enumerate(marks):
    print(index,marks)
