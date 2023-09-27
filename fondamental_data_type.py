### Fundamental Data types

## Int & float
# float takes larger space in memory than an integer
type(2+4) #int
type(2-4) #int
type(2/4) #float
type(9.8 + 0.2) #float

2 * 3 
2 ** 3 # exponential (2 power of 3 )
5 / 4  # rounded down to an integer so equals to 1
5 % 4  # modular gives the remain of a division so equals to 1


## Math Functions
round(3.9) 
abs(-20)  # returns the absolute value of an argument (absolute value = no negative ) so the answer is 20


## operator precedence 
# Please Excuse My Dear Aunt Sally 
# Please : Parentesis  ()
# Excuse : Exponentials  **
# My : Multiplication  *
# Dear : Division  /
# Aunt : Addition  +
# Sally : Subtraction  -

bin(5)  # returns the binary representation of a number
int('0b101', 2) # convert that binary number to a base 2 number

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
c = type(b)
print(c)

#or 
print(type(int(str(100))))

## Escaping sequenc

weather = 'it\'s a kind of \"summer\" in here'
'\t hello' # hello will be print with a tab-space befor
'\n' # new line
