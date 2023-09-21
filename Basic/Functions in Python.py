#import keyword
#print(keyword.kwlist)

def hello_func():
    print("Hello Function without argument")
hello_func()

def return_func():
    return 'This function is return something'
print(return_func())
print("Return function with upper case: ",return_func().upper())

def argument_func(greeting):
    return '{} This is an argument Function.'.format(greeting)
print(argument_func('Hi!'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Math','Art',name ='Adil', age =50)

courses = ['Math', 'Art']
info = {'name': 'Adil', 'age': 32}
student_info(*courses,**info)
