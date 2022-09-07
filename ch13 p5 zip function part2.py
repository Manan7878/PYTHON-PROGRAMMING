'''now we will study what more things we can do with zip function'''

# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
l = [(1,2), (3,4), (5,6), (7,8)]
# we want to make two lists like l1 and l2 from l
# we can make them with zip function using star operator with zip

# list(zip(*l))
'''
dong this will unpack the list and will make two tuples the first will contain 1,3,5,7 and the second will contain 2,4,6,8
and then i converted it into a list
'''
# what we have is a list of two tuples but now we want to seperate those two and make them both lists

l1 , l2 = list(zip(*l))
'''so we will get two objects the first will go to the first variable and the second will go to second variable'''

print(list(l1))
print(list(l2))

'''what we want to do is create a new list in which the greater number will be stored'''
new_list = []
for i in zip(l1,l2):
    new_list.append(max(i))
print(new_list)
'''
elements on the zero position from both list will go to the loop then the position 1 then 2 and so on
so 1 and 2 will go first 
2 is greater so it will be appended o the new list
and this will go till one of the list or both the lists end
'''

