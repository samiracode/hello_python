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
def sum (num1, num2) :
    def another_fun (n1, n2) :
        return n1 + n2
    return another_fun(num1, num2)
total = sum(10,20)
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




