# in this file we will learn about how to add and delete data in dictionaries

user_info = {
    'name' : 'manan',
    'age' : 14,
    'fav_fruit' : 'mango'
}

# to add data 
'''
first type name of the list  and in brackets write the key to add then equals sign then the value you want to assign to that key you typed
'''
user_info['fav_songs'] = ['song1', 'song2']


'''
there are two methods to delete data from a dictionary
1st method is pop method
but pop method returns the value of the key we removed so we can store it in a variable
'''
pop = user_info.pop('fav_songs')# so now fav_songs have been popped from the list 
# we can print it also
# the type of the item removed it returns is a list


'''
2nd method is popitem
it will remove a random key value pair from dictionary
in this also we can store the randomly poppeditem in a variable
'''
poppeditem = user_info.popitem()
print(poppeditem)# the type of the popped item it returns is tuple