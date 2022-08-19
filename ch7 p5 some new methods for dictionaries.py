'''
methods we are going to learn in this file are as follows



1st -----> fromkeys
fromkeys method is used to create dictionaries in which all keys have same values


2nd ----->get
get method is used to access data from the dictionary


3rd ----->clear
clear method is used to empty the out whole dictionary


4th ----->copy
copy method is used to make a copy of a dictionary


'''


#1st   fromkeys
'''
first in a list type the keys you want to add in the list and then outside the list after a coma type the value you want to assign to the keys
'''

d = dict.fromkeys(['name', 'age', 'height'], 'unknown')# if you don't want to use list you can use tuples also
'''now all the keys have the value unknown'''

'''we can use range function also'''
a = dict.fromkeys(range(1,6), 'unknown')# there will be keys 1,2,3,4,5 and they all have the value unknown


# 2nd   get
'''
first this method is very useful because when we acces data normally by brackets and emter data which does not exist so it gives us error
but with get method it gives the output none which means there is no such thing 
'''
print(a.get('6'))

# 3rd clear

b = {'a':'b','c':'d'}
b.clear()
'''so now the whole dictionary is empty'''



# 4th   copy
'''copy method is used to make a copy of a dictionary'''
d1 = d.copy()
'''so now d1 is a dictionary which has the same data as the dictionary d'''


'''
many people will assign
d1 = d
so now d1 and d are both the same dictionary
either you work with d1 or d the work will be done with the original d
but with copy method a new dictionary will be created
'''

