### Data Structures
# Data structure is a specialized format for organizing, processing, retrieving and storing data.

## Lists
# Lists are like sort of arrays in JS 
amazon_cart = ['notebook', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[1])

## Slicing Lists
# [start:stop:stepover] is also valid here but lists are changble so we can reassign new values to them.
amazon_cart[0] = 'laptop'
print(amazon_cart)
new_amazon_cart = amazon_cart
print(new_amazon_cart)  # with slicing we are creating a new list
new_amazon_cart[0] = 'gum'
print(amazon_cart)
# after new_amazon_cart = amazon_cart, if we do changes to one, we are changing also the other one
# how ever if we want to avoide that we should write new_amazon_cart = amazon_cart[:] 

## Matrix : Multi dimentional list 
matrix = [
    [1,2,3],  # <= sublist
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

# question: what is an object in Python? everything

basket = [1,2,3,4,5]
print(len(basket))