'''so now we will study set comprehension'''
'''it is really easy to understand'''
'''let's take the old example of squares of 1 to 10 '''
s = {k**2 for k in range(1,11)}
'''this is how we can create set by set comprehension'''

'''but if we print it, the order will be changed'''
print(s)



l = ['manan', 'rohan', 'sohan']
'''now we have a list and we want to make a set of the first character of every name or string'''
first = {i[0] for i in l}


