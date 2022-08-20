s = {'a', 'b', 'c'}
'''if you want to check for any item that it is in your list or not'''
'''so we will do it as it is as we don it with lists'''
if 'a' in s:
    print('present')
else:
    print('not present')# so it will print present


'''we can run a loop also in a set'''
for i in s:
    print(i)
'''but you will find that everytime you run the loop it is printed in different orders'''
'''this is why set is unordered collection'''


'''we can also perform mathematical operations in sets'''

'''
we can perform two things
1st----->union
we use union to combine two stes and we can store it also

2nd----->intersection
we use intersection to find or store common values from the two sets
'''

#1st union
s1 = {1,2,3,4}
s2 = {3,4,5,6}

s3 = s1 | s2 # we use pipe symbol to do union
'''now they are combined but a set cannot contain duplicate values so it will remove 3 and 4 '''
'''if i print s3 the output will be -----> {1,2,3,4,5,6}'''


#2nd intersection
'''we use and sign for intersection'''
print(s1 & s2) 
'''so the output will be -----> {3, 4}'''


