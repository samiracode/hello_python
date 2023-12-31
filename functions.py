### Functions
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def show_tree():
    for row in picture :
        for pixel in row :
            if  pixel == 1:
                print('*', end='') 
            else :
                print(' ', end='') 
        print('') 

show_tree()
print(show_tree)

# Positional Parameters (they are called positional because their position matters)
def say_hello (name, emoji) :
    print(f'Hello {name} {emoji}')

# Positional Arguments
say_hello('Charlie', ':)')
say_hello('Leonard', ':D')
say_hello('Sally', ':p')

# Keyword arguments (position does not matter) => bad practice !!!
say_hello(emoji=':)', name='Andrei')

# default parameters (incase we call the function and we do not give any argument, the default argument will be run)
def say_hello1(name="Arthur", emoji='xD ') :
  print(f'Hello {name} {emoji}')

## Return 
# a function weather modifys something or returns something
def add_nums (num1, num2) :
    def another_fun (n1, n2) :
        return n1 + n2
    return another_fun(num1, num2)
total = add_nums(10,20)
print(total)

## tesla exersize :


def turn_on_engin () :
    age =input('How old are you?')
    driver_age = int(age)
    if driver_age <18 :
        print('Sorry, you are not old enough! Powering off!')
    else :
        print('enjoy the ride')

turn_on_engin()

## Docstring
def test(a) :
    '''
    this function test & prints parameter a
    '''
    print(a)

test('!!!!')

help(test)
# or magic method or dunder method
print(test.__doc__)

## Arguments & keyword arguments
 # *args & **kwargs


def super_func(*args):
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

def duper_func(*args, **kwargs) :
    total = 0
    for item in kwargs.values() :
        total += item
    return sum(args) + total

print(duper_func(1,2,3,4,5, n1=6, n2=7))

# Rule for using parameters in function
# First parmaeters
# Second **args
# Third default parameters
# Fourth **kwargs

## Ex:
def highest_even (li) :
    evens = []
    for n in li:
        remain = n % 2
        if remain == 0 :
            evens.append(n)
    if evens == []:
        print('There is no even numbers in the list')
    else :
        print(max(evens))

highest_even([1,3,5,7,8,4,6,12])

## Walrus Operator (:= )
a = 'Helllooooo'
if len(a) > 5 :
    print(f'this is {len(a)} long element. Too long!')

if((n := len(a)) > 5) :
    print(f'this is {n} charachter long. I am not gonna print this')

while ((n:= len(a)) > 1) :
    print(n)
    a = a[:-1]
print(a)

## Scope ; which variables do we have acces to 
#1 start with local 
#2 parent local
#3 Global
#4 built in python functions

n = 1

def parent () :
    n = 10
    def confusion ():
        return n
    return confusion ()

print(parent())
print(n)

## Global Keyworld
# local & nonlocal
total2 = 0 
def count():
    global total2
    total2 += 1
    return total2

count()
count()
print(count())
# the above example is not a good way of practice 
# a better way is called "dependency injection"
# the previous block of code was giving an output of 3
# we re-write the code above with dependency injection and get the same result:

total3 = 0
def count2(total3) :
    total3 += 1
    return total3

print(count2(count2(count2(total3))))

# the nonlocal keyword is refering to parent local
def outer() :
    x = "local"
    def inner ():
        nonlocal x
        x = "non local"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()



    
    
     

            

            

           


