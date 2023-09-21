#---In this program we have all about the strings in python---

#Print Hello world in Python
print('Hello World')

#String variable in String
message = 'Hello World'
print('Print a string variable that have a message',message)

#print('Hello's World') Error in this line because of a single quote
print("This write in double quote to avoid the error Hello's World")

#Len Function
print('Length of a variable message is: ',len(message))

#Print a specific character of a string variable
print('message have a character in index 0 is: ',message[0])
#Error occur if index have not a character like message[12] index out of range error occur

#Range of string 
print('Print first 5 character of a string variable message: ', message[0:5])
print('Print first 5 character of a string variable message: ', message[:5])
print('Print after 6th index of a string variable message: ', message[6:])

#Lower & Upper case
print('Print in lower case', message.lower())
print('Print in upper case', message.upper())

#Count method
print('Times of l appears in message variable is: ', message.count('l'))

#Find method
print('This function gives the index where it appears: ',message.find('l'))

#Replace method
print('Replace the World with universe in message: ', message.replace('World','Universe'))

#Concatenate
greeting = 'Hello!'
name = 'Adil'

print(greeting + ' ' + name)

#F string function is usefull to use the string function directly to the variables
message = f'{greeting.upper()} {name}  Welcome.'
print(message)

#It shows how  many methods and attributes are use with the string
print(dir(name))

#It gives the details about the above functions
print(help(str))

#Last two are the important and very useful in python with respect to the string variables