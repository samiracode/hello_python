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
new_basket = basket.append(100)
print(new_basket) #None!!!! we should append befor we assign it to new_basket

basket.insert(3,500)
print(basket)

basket.extend([300, 400, 500])
print(basket)

basket.pop()   # pops off whatever is at the end of the list
print(basket)

basket.pop(0)
print(basket)

basket.remove(100) # this method takes a value, not an index
print(basket)

new_list = basket.pop(4)
print(new_list) # it gives me 5 but if I use remove method instead I get None because remove method
# modify the list in place and pop method not, it also takes an index instead of a value of the list

basket.clear()
print(basket)

book = ['a', 'b', 'c', 'd', 'e', 'a']
print(book.index('c',0, 3)) # index (value, start, stop)
print('e' in book)
print(book.count('a'))
book.sort()
print(book)
# if we do print(book.sort()) we get Non but if we do print(sorted(book)) we get the list sorted for us
# sorted() creats a new copy of book but sort modifys it in place
new_book = book.copy()
print(new_book)
book.reverse()  # it is reversing the place of indexes [index4, index3, index2, index1, index0]
print(book)
print(book[::-1])  # this is also reversing the list but creats a new copy and the main list is not modified

## Range
print(list(range(0,20))) # range(start, stop)

sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Gigi'])
print(new_sentence)

## List unpacking 
# assigning a variable to each value in the list
a,b,c, *other, d = [1,2,3,4, 5, 6, 7, 8, 9, 0]
print(b)
print(other)