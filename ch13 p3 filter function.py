'''now we will study about filter function'''


'''it will return true if the number is divisible ny 2 and will return false if the number is not divisible by 2'''
def even(a):
    return a%2==0
numbers = [3,4,2,1,5,6,9,8,10]
'''
what you have to do is
create a list evens in which there are all the even numbers from the list numbers
'''

# normal way
evens = []
for a in numbers:
    if a%2==0:
        evens.append(a)
print(evens)
'''
this way is the normal way in which every time the loop runs it will check the number is even or not if it is then it will be appended to the list
'''

# we can do this with the filter function
evens2 = tuple(filter(even, numbers))
print(evens2)# this is very short code compared to the previous one 

'''
if you directly print it like map so it will give you filter object
so to prevent that we converted it into a list
'''

'''we can also use lambda in this also'''

evens3 = tuple(filter(lambda a: a%2==0, numbers))
print(evens3)

# filter object is also iterable so we can run loop in this too
evens4 = filter(lambda a : a%2==0 , numbers)
for i in evens4:
    print(i)
# note :    filter object is also just like map it can only run one time
'''
but if we convert it into a list or a tuple so we can run loop in it as many times as i want
'''

'''we can also do it with list comprehension'''
evens5 = [c for c in numbers if c%2==0]
print(evens5)


