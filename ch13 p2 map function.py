'''now we will learn about map function'''
nums = [1,2,3,4]

def square(a):
    return a**2

squares = tuple(map(square, nums))
print(squares)

'''
so now map function is using the pre defined function square with the list nums
it is acting like a list 
first it will take 1 and print its square
then it will take 2 and print its square
'''

'''
note : you cannot use map with print first you have to store it with a variable and make it a list or a tuple
after that you can print it with the help of the variable
'''

'''this is why we learned lambda expression instead of defining a function before using map we can use it in the map '''
squares2 = list(map(lambda a:a**2, nums))
print(squares2)
'''so this is how we can use lambda with the map function'''

# we can also do this with list comprehension 
# so let's do it
squares3 = [num**2 for num in nums] 
# this is how we can do it with list comprehension 
# if you want to try is with set comprehension you can try that too


# now let's try to do it without comprehension or map function
square4 = []
for num in nums:
    square4.append(num**2)
print(square4)
# this is also a way to do it



l = ['abc', 'abcd', 'abcde']
'''
now waht we want to do is
find length of every string present in the list l
'''
# for finding out length we already have a function len
print(map(len, l))# now it will give me a map object
'''map object is also a iterable so we can run a loop in it too'''

length = map(len, l)
for i in length:
    print(i)
# it will give output one by one for every string

# note :        on map object you can run a loop only once
'''the loop i entered after that if i do one more loop so it will do nothing'''
