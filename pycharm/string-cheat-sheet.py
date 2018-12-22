# How to  create a strin in python?

my_string = 'hello'
print(my_string)

my_string = "hello"
print(my_string)

my_string = '''hello'''
print(my_string)

my_string = """hello"""
print(my_string)

# format string in python
name = 'x'
print(f"Hello {name}".format('name = name'))

# how to access characters in a string?
string1 = 'programming'

#first character
print('string1[0]', string1[1])

print('string1[-1]', string1[-1])

#ตัวที่2-5
print('string1[1:5]', string1[1:5])
#ตัวที่6ถึง2
print('string1[5:-2]', string1[5:-2])
# string is immutable
my_string = 'hello'
# my_string[0] = 'a' This is not correct !

#delete the entire string
del my_string

#how to concatenate two strings
string1 = 'hello'
string2 = 'world'
print('string1 + string2 = ', string1 + string2)

#iterate through a string
count = 0
for letter in 'hello world':
    if letter == 'l':
        count += 1
print(count, 'letters found')

#string membership test
print('a' in 'programming')

print('pr' not in 'programming')

#built-in functions of python
print('len(string1 = ', len(string1))

#enumerate a string
print('list(enumerate(string1))', list(enumerate(string1)))

#escape special symbols
# He said, "what's there?"
print('He said, "what\'s there?"')
print("He said, \"what's there?\"")

# format string in python
name = 'x'
print(f"Hello {name}".format(name=name))

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))


