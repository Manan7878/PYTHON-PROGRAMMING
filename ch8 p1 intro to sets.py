'''in this file we will learn about sets'''
'''set ia a data type'''
'''set is a unordered collection of unique items'''
'''we can create a set with the use of curly braces'''
'''but in this we do not have key and value pair'''
'''in a set an item cannot be repeated if you type same more than one time it will only be considered once'''
'''this is why sets are called unordered collection of unique item '''
s = {1,2,3,4,2,3,5, 'a', 'b'}# but if you print it it will consider all the repeated items once
'''this is how you can create a set'''
'''unordered collection means you cannot do slicing in this'''


'''now if you have a list where you have duplicate items too you can remove them by sets'''
l = [1,1,2,3,4,5,5,5,5,6,6,9]
s2 = set(l)# here i used set function to convert my list into a set



'''and you can even convert the set into the list at the same time you converted the list into the set to remove the duplicates'''
l2 = [1,1,2,2,3,3,4,4,5,5,6,6]
ab = list(set(l2))



'''so now let's talk about some methods for sets'''
'''now i have to add some data to the set so we will use add function'''
s.add(4)# so now there is 4 in the set too
'''even if you add an item more than one time it will be considered as once'''

'''what if i want to remove something from the set'''
'''so we use remove method'''
s.remove(3)# now 3 is not in the set

'''but what if you write something which is not in your set'''
'''so it will give a error'''

'''but if you don't want error'''
'''so we use discard method'''
s.discard(7)# it will not give any error

'''if you want to remove all the items from the set'''
'''so we use clear method'''
c={1,2,3,4,5}
c.clear()# now there is nothing in the set c

'''we can also make a copy'''
s3 = s.copy()


'''now let's talk about what type of data we can store in sets'''

'''
we can store integers, floating values and strings
but we cannot store lists, dictionaries and tuples inside sets
'''

abcd = {1,1.0,2.2,'abcd'}# nut when you print this it will take 1 and 1.0 as same values

