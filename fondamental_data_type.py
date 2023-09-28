### Fundamental Data types

## Int & float
# float takes larger space in memory than an integer
type(2+4) #int
type(2-4) #int
type(2/4) #float
type(9.8 + 0.2) #float
print(type(9 + 2.1))

2 * 3 
2 ** 3 #  2 power of 3 
5 / 4  # rounded down to an integer so equals to 1
5 % 4  # modular gives the remain of a division so equals to 1


## Math Functions
round(3.9) 
abs(-20)  # returns the absolute value of an argument (absolute value = no negative ) 


## operator precedence 
# Please Excuse My Dear Aunt Sally 
# Please : Parentesis  ()
# Excuse : Exponentials  **
# My : Multiplication  *
# Dear : Division  /
# Aunt : Addition  +
# Sally : Subtraction  -

bin(5)  # returns the binary representation of a number
# int('0b101', 2)  convert binary number to a base 2 number

## variables

# constants variables are writen in capital letters
PI = 3.14
# we can overide them for sure but that is not a good practice

# dunder variables; we should not creat a varibles that starts with duble under scores like:
__hihi = 'hi'

# short way to assign values to more than one variables:
a,b,c = 1,2,3

## Expressions vs Statements
# expression is a piece of code that produces value
iq = 180
iq/5 # this is an expression
# a statement is an entire line of a code like
user_age = iq/5 # this is a statement

## augmented assingment operator
some_value = 5
some_value += 2
print(some_value) #the answer is 7 

## strings are written like in JS but there is an additional type: long string
long_string = '''
WOW
O O
---
'''

## string concatenation
'samira' + ' tavakolli' 

## Type conversion : converting to str or int
a = str(100)
b = int(a)
c = float(b)
d = type(c)
print(d)

#or 
print(type(float(int(str(100)))))

## Escaping sequenc

weather = 'it\'s a kind of \"summer\" in here'
'\t hello' # hello will be print with a tab-space befor
'\n' # new line

## formatted strings 
name = 'Johnny'
age = 55 
print(f'hi {name}. You are {age} years old')
# or
print('hi {}. You are {} years old.'.format(name, age))
# or
print('hi {1}. You are {0} years old.'.format(name, age))
# or 
print('hi {new_name}. You are {sally_age} years old.'.format(new_name = 'Sally', sally_age = 100))

## string indexes
bunch_of_numbers = '01234567'
print(bunch_of_numbers[4])    # prints 4
print(bunch_of_numbers[2:6:2])# [start:stop:stepover]
print(bunch_of_numbers[1:])   # prints from 1 till end
print(bunch_of_numbers[:5])   # prints from start till 5
print(bunch_of_numbers[::1])  # default behavior
print(bunch_of_numbers[-1])   # prints 7; negative means start from end
print(bunch_of_numbers[::-1]) # prints 76543210 minus means stepover from end
print(bunch_of_numbers[::-2]) # prints 7531

## immutibility : strings in python are not changable

## build in functions and methods

# calculating the length of a string
len('hellloooooooo')
greet = 'helllooo'
print(greet)
print(greet[3:len(greet)]) 

# print() is a build in function
# something.format() is a build in string method

quot = 'to be or not to be'
print(quot.upper())
print(quot.capitalize())
print(quot.lower())
print(quot.find('be')) # does 'b' exist? answer: 3 (starts at index 3)
print(quot.replace('be', 'me'))
print(quot) # will print the first value str we had because str are immutable

## Boolean

print(bool(0))  #False
print(bool(1))  #True

## Facebook excersize

birth_year = input('Which year were you born?')
year_number = int(birth_year)
how_old = 2023 - year_number 
print(f'Congratulations! you are {how_old} years old.')

## Passworld checker excersize

username = input('Please enter your name')
passworld = input('Please enter your passworld')
passworld_len = len(passworld)
hide_passworld = '*' * passworld_len

print(f'Hi {username}. Your passworld is {hide_passworld} is {passworld_len} letters long')