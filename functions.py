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


