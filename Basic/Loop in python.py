num = [1,2,3]
for n in num:
    print(n)

#Break condition
for n in num:
    if(n == 2):
        print("found!")
        break
    print(n)

#Continue condition
for n in num:
    if(n == 2):
        print("found!")
        continue
    print(n)

#Nested loop
for n in num:
    for letter in "abc":
        print(n,letter)

#Define range
print("Start from 0: ")
for n in range(10):
    print(n)

print("Start from 1: ")
for n in range(1,11):
    print(n)

#while loop
x = 0
print("While loop:")
while(x < 10):
    print(x)
    x +=1

#while True:
#   print("Infinite loop for cancle infinite press ctrl c")


