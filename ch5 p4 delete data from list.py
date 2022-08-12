# in this file i will show you how to delete data from list

fruits = ['apple', 'mango', 'litchi', 'orange', 'grapes', 'kiwi', 'banana', 'pear']

# there are three ways to delete data from the list

# first is pop method
fruits.pop(0)# it will remove apple
# remember if you don't write position in the brackets it will delete the last thing

# second is del operator
del fruits[1]# so it will remove litchi because apple was removed and now litvhi is at the 1 position

# third is remove method
fruits.remove('banana')# if there are twoo banana in the list then it will delete the first one


print(fruits)