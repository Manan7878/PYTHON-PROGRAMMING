fruits = ['grapes', 'mango', 'apple']
'''we learned about a method sort earlier '''
fruits.sort()
print(fruits)# sort method will sort my list alphabatically
# but sort is not available with tuples if we try to do it with tuples it will give an error

# so we have sorted function
fruits2 = ('grapes', 'mango', 'apple')
# but tuples are immutable
print(sorted(fruits2))
# this will sort the fruits alphabaticallybut in the return it will give us a list

# same with the sets
fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))
'''
but as you know sets do not have orders that is why they are are unordered collection of sets
but you can still print them with order by sorted function
in the output this will also give us a list
'''


games = [
    {'name': 'pacify', 'size' : 2.5},
    {'name' : 'GTA V', 'size' : 66},
    {'name' : 'hello neighbor', 'size' : 1.5}
]
# now i want to sort this by min so thta the game which has the minimum size should come first
# to sort this we have to use lambda with min max function
print(sorted(games, key = lambda i : i['size']))

# if i use reverse in it so it will do just the opposite
print(sorted(games, key = lambda i : i['size'], reverse = True))