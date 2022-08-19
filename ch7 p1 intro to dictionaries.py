# in this part we will learn about dictionaries
# we use dictionaries because of the limitations of lists and lists are not enough to represent real life data 

# dictionaries are unordered collection of data

a = ['manan', 14, ['ab', 'cd'], ['ef', 'gh']]
# this is a list which has my name age list inside list and list inside list but it does not declare that this element is this 
# and thus it is not a good way to do this

# we can create dictionaries by using braces or we can say curly brackets -- >{}
# in dictionaries everything is assigned but still is a unordered collection of items
user_info = {'name':'Manan', 'age':14}# so in this the key values are name an age
# manan is assigned to name and 14 to age

# second way to create dictionaries
# now we will create a dictionarie named user2
user2 = dict(name = 'abcd', age = 1234)

'''
always remember when we create dictionaries by using dict function the key values are not kept in inverted comas and equal sign is used 
instead of columns
'''

# we can also create dictionary like this
dictionary = {
    'name' : 'manan',
    'age' : 14,
    'favourite movie' : 'unknown'
}# just hit enter like this
# just don't forget to put a coma after every line you type 


'''
now let's see how can we access data in a dictionary
because in dictionaries we cannot do slicing
we can access data by using key values instead of positions of elements
'''
print(user2['name'])# so the output will be abcd

'''
what type of data can we store in dictionaries ??
we can store any type of data in dictionaries
we can also store a dictionary in a dictionary
'''

something = {
    'movies' : ['a', 'b'],
    'songs' : ['c', 'd']
}


# now let's see how can we add data into empty dictionaries
empty = {

}
empty['name'] = 'abcd'
empty['age'] = 14
# now the key is name and abcd is assigned to it
print(empty)



