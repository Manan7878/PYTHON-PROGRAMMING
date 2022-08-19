# in this file we will learn about looping  and in keyword in dictionaries

user_info = {
    'name' : 'manan',
    'age' : 14,
    'fav_movies' : ['a', 'b']
}

# first we will check if there is a name key in the dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')
# so it will print present but if you type something that is not in your dictionary so it will print not present


# now let's check for a particaular value in our dictionary
if 'manan' in user_info:
    print('present')
else:
    print('not present')
# so it will print not present necause it does not check for values
# so here we will use value method

if 14 in user_info.values():
    print('present')
else:
    print('not present')
# so now it will print present


# if you want to check for a list you have enter the list
if ['a', 'b'] in user_info.values():
    print('present')
else:
    print('not present')


# now let's perform some loops some loops
for i in user_info:
    print(i)# so it will print all of the keys

# but if you want to print values you can use values method
for i in user_info.values():
    print(i)# so it will print all the values



# now let's see if we can store them in variables
user_info_values = user_info.values()
print(user_info_values)# it prints something like lists but not lists 
# now let's check their type
print(type(user_info_values))# so it will print dict values

# now keys
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))# this also prints like a list 
# but their type is dict keys
'''
 now let's talk about items method 
 most important method of all
'''

user_items = user_info.items()
print(user_items)
print(type(user_items))

'''
what actually items method do it is that it reaturns a list which contains tuples
but its type is dict itmes
it is actually printing the pair of keys and values
'''

for key, value in user_info.items():
    print(f'key is {key} and value is {value}')
'''
so what will happen is that key will go into the key variable and value will go into value variable
'''




