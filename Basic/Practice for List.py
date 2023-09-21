#1) Write a Python program to sum all the items in a list.
marks =[100, 90, 85, 59,60]
print('Sum of the lists marks is:',sum(marks))

#2) Write a Python program to multiply all the items in a list.

def multiply_marks(marks):
    tot = 1
    for x in marks:
        tot *= x
    return tot

print('Multiply of lists elements: ', multiply_marks(marks))

#3) Write a Python program to get the largest number from a list.
print('The largest number from a list:',max(marks))

#4) Write a Python program to get the Smallest number from a list.
print('The Smallest number from a list:',min(marks))

#5) Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

strings = ['abc', 'aba', '1001', 'lol']

def match_string(strings):
    count = 0
    for string in strings:
        if(len(string) > 1 and string[0] == string[-1]):
            count += 1
    return count

print(match_string(strings))