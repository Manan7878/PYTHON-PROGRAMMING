fruits1 = ['mango', 'orange']

# to add data to a particular place in a list we use insert method
fruits1.insert(1,'litchi')# now at the position no. 1 we will have litchi

# now we will create one more list
fruits2 = ['kiwi', 'apple']

# to add data from one list to another list we use extend method
# always remember that when you use extend method all the data are added 
fruits1.extend(fruits2)# now all the data from fruits2 are also in fruits1
