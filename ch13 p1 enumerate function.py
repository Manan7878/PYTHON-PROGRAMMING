'''now we will talk about enumerate function'''
# note :        we use enumerate function with for loop
'''we use enumerate function to track position of our item in iterable'''


names = ['abc', 'abcdef', 'manan']
'''
we want to print something like
0 ---- > abc
1 ---- > abcdef
2 ---- > manan
what i mean is print the items with their positions
'''

pos = 0
for name in names:
    print(f'{pos} ---- > {name}')# if we start the loop the pos wwill always be zero 
    pos += 1    # everytime the loop runs the pos will be increased by 1
'''i hope you understand how it works'''


# now let's do it with enumerate function
for pos2, name2 in enumerate(names):
    print(f'{pos2} ---- > {name2}')
'''as you can see the code is very small now a compared to the previous one'''
'''
what it is doing is
we took two variables the first one tracking position so with enumerate function python knows the variable we first entered is for tracking and
its value is zero for default every time the loop runs its value increases by 1

the second variable is for the loop as we know
'''
