'''
list comprehension is used make list in a sing line
with the normal way it actually takes time
like when you have to create a list in whic we have to append squares of all numbers between 1 to 10
'''

# normal way
squares=[]
for i in range(1,11):
    squares.append(i**2)
'''
as you can see it takes too much time
but with list comprehension we can do it easily
'''


'''
now let's see how list comprehension works
first create a list type what you want to append and after that type the for loop
'''
squares2 = [i**2 for i in range(1,11)]# the other way it means that we want to append square of i and i is in range of 1 two 11

'''
now let's talk about one more example
in this you have to create a list in which you have to print all the negative numbers from -1 to -10
'''

# normal way
negative = []
for i in range(1,11):
    negative.append(-i)

# with list comprehension
negativve = [-i for i in range(1,11)]


names = ['manan', 'yukti', 'abcd']

'''
now let's do something interesting
i have to create a new list in which you have to append all the first characters of every string from the names list
'''

# normal way
new_names = []
for i in names:
    new_names.append(i[0])


# using list comprehension
names2 = [i[0] for i in names]



