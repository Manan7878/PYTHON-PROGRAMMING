'''so now we will study about zip function'''
users = ['user1', 'user2', 'user3']
names = ['manan', 'mohit', 'rohit']


'''
in the 1st list we have 3 users
in the 2nd list we have the names of the users
and now somehow we want to attac users to their names or we can ssay we want to zip the users with their names
'''
# for that we have zip function

'''
zip function will give us a zip object
in which we have tuples
like ('user1', 'harshit'), ('user2', 'mohit'), ('user3', 'rohit')
and we can covert this zip object into a list or a tuple
'''

# so now let's try to use it
zipped = tuple(zip(users, names))
print(zipped)# now we will get a tuple in which there are many tuples 

# now let's see what happens when we enter names first and then users list
zipped2 = tuple(zip(names, users))
print(zipped2)
'''
what will happen now is in every tuple strings from the names list will be given first
'''

# now let's see what happensif there is a list which have less elements
a = ['a', 'b', 'c']
b = ['d', 'e', 'f', 'g']# now what will happen
print(list(zip(a, b)))
'''so now zippin will stop when a list or a tuple is over'''
'''so in the output you will not see g or a error'''

example = [('a', 1), ('b', 2), ('c', 3)]
# you can convert this type of list into a dictionary or just print it like a dictionary
print(dict(example))# now example will be printed as a dictionary

'''
by this what i am trying to tall you is this where you converted the zip object to a list or a tuple you can convert it into a dictionary
'''

c = [1,2,3]
d = ['a', 'b', 'c']
e = [4,5,6]
print(dict(zip(d,c)))

# you can also do it with 3 lists or tuples but not dictionaries because it requires two things taht are keys and values not anything else
# i hope you understand
print(tuple(zip(c,d,e)))
'''you will see that in every tuple there is one more element'''

