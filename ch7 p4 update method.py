user_info = {
    'name' : 'manan',
    'age' : 14,
    'fav_fruit' : 'mango'
}

more_info = {'a' : 'b', 'c' : 'd'}
'''
now i have two dictionaries 
and I want to add the data of the 2nd dictionary to the 1st dictionary
so i will use update method
'''

user_info.update(more_info)

''' so now the data from the 2nd dictionary is now in the 1st dictionary'''
''' but what if there is a same key in the 2nd dictionary'''

a={'age':16}

user_info.update(a)

'''so now the key age will be updated 
if we print the dictionary it will print the age 16 '''

print(user_info)

