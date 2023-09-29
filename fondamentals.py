## Conditional logics

is_old = True
is_licenced = False

#if is_old : 
#   print('you are old enough to drive this car')
#elif is_licenced :
#    print('you are good to drive')
#else : 
#   print('Sorry! you can not drive this car')

if is_old and is_licenced :
    print('Have a good drive!')
else :
    print('Sorry! You can not drive this car')

# Truthy & Falsy values 
username = 'samira'
password = '123'
if username and password : # we are checking if thoese values exist; they are truthy
    print('Welcome to your page')
else : 
    print('Please sign up for an account')
# we can check truthy & falsy values on documentations

## Ternary Operators
# condition_if_true if condition else condition_else
is_friend = False
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(can_message)

## Short Circuiting (or)(and)
# (or) if one condition is correct, py does not check the second one
# (and) if one condition is false, py does not check the other condition
is_close = True
is_economy = True
if is_close or is_economy : 
    print('good! Let\'s go there')
else :
    print('I just don\'t feel like to join you')

## Logical operators
# and, or, not, <, > , ==, !=, >=, <=, 
print('a' > 'b')
print('a' > 'A')
print(not (False)) # not is also a function

is_magition = True
is_expert = False
if is_magition and is_expert :
    print('You are a master magition')
elif is_magition and not is_expert :
    print('At least you are getting there')
elif not is_magition :
    print('You need some magic!')

## is vs == 
print(True == 1) # True
print('1' == 1)  # False
print([] == 1)   # False
print(10 == 10.0) # True
print([] == [])   # True
print([1,2,3] == [1,2,3]) # True

#print(True is 1)
# if we make all the == above to 'is', they all ended up false
# because == compares the values of but 'is' is pointing at a place in memory 
# Where all these values are alocated, as they can not be the same, it prints False
print ([] is []) # False
# print(value is value) True
# print( data_structure is data_structur) False

## For Loops 
for item in "samira is a ..." :
    print(item)
for item in [1,2,3,4,5] :
    print(item)
    print(item)
    print(item)
print(item)     # 5 gets printed 4 times!

for item in (1,2,3,4,5) :
    for x in {'a','b','c'} :
      print(item, x)
      
## ITERABLE can be a list, dictionary, set, string, tuple

user = {
    'name': 'Samira',
    'age': 5008,
    'can_swim': True
}
for item in user :
    print(item) # it prints out only the keys but what if we want the values as well?
# dictionaries have 3 methods when it comes to iterate thru them;
for item in user.items() :
    print(item)
for item in user.values() :
    print(item)
for item in user.keys() :
    print(item)
for key, value in user.items() :
    print(key, value)

## Excersize 
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for num in my_list :
    sum = sum + num
print(sum)

## RANGE FUNCTION : is a special object that rerurns an object that produces 
# a sequence of integers from start to stop
for number in range(0,11) :
    print(number)

for _ in range(0,11,2) :
    print(_)

for _ in range(10,0,-2) :
    print(_)

for _ in range(10,0,-2) :
    print(list(range(10)))

## ENUMERATE wraps around an object and returns an object that is enumerated. we should give an iterable object
# to enumerate over it.
for i, char in enumerate('Haaallllååååå') :
    print(i, char)

for i, char in enumerate(list(range(100))) :
   if char == 50 :
       print(f'The index of 50 is : {i}')

## WHILE LOOP 
i = 0
while i < 20 :
    print(i)
    i += 1
    # break ( if we had a break here and we do not use else, the line down would never execute)
else :
    print('Done with all these work here')
# while True :
    # do something
    # break

while True :
    responce = input('say something: ')
    if responce == 'bye':
      break

## Break, Continue, Pass
## Excersize GUI print a christmas tree
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for row in picture :
    for pixel in row :
        if  pixel == 1:
            print('*', end='') #the end here is keeping a star in place
        else :
            print(' ', end='') # the end here is keepin empty space in place
    print('') # need a new line after every row

## Clean Code : follows a style that python community endorses 
# Readibility : if you come back after 2 years are you still able to read that code?
# Predictibility : use latest features
# DRY

## Excersize : Find the dupplicate
some_list = ['a', 'b', 'c','b', 'd', 'm', 'n', 'n']
dupplicates = []
for value in some_list :
    if some_list.count(value) > 1 :
        if value not in dupplicates :
            dupplicates.append(value)
print(dupplicates)


    
   
