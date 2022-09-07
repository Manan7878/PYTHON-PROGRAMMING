'''
now we will study more about min and max function
we know that max function finds the maximum amount
'''

numbers = [1,2,3,4,5,6,8]
print(max(numbers))
# in the output we will get 8

names = ['manan', 'harshit', 'abc', 'z']


'''
what we want to do is find which string has the maximum length in the names list
so now we will use the max function
'''
print(max(names))# it will give the output z because it at the maximum length of the list 
'''but what we want is to print which string has the maximum length'''

# for this we will use another function which we will define ourself
def func(i):
    return len(i)
# what will this do is it will take i and return i with len function 
# length function is used to measure length in python
'''
when we will use max we will use the function we designed
'''
print(max(names, key = func))# we use key to use max and min function to find max and min in what way we want to find
# note :    do not use parenthesis when recalling your function in the key
'''min function is just the opposite of max function it tries to find the minimum value in the data we entered'''
print(min(names, key = func))# the output will be z

# now we will do this with lambda 
names2 = ['a', 'ab', 'abc', 'abcd', 'abcde']
print(max(names2, key =  lambda i : len(i)))
'''it is also the same as the function we defined previously and we will do the same with min function'''
print(min(names2, key =  lambda i : len(i)))


students = [
    {'name' : 'manan', 'score' : 100, 'age' : 14},
    {'name' : 'rohan', 'score' : 90, 'age' : 14},
    {'name' : 'sohan', 'score' : 95, 'age' : 14}
]
'''
i have a list which contains several dictionaries
now i want to print who has got the maximum score
'''
print(max(students, key = lambda i : i.get('score')))
# if i want to print a specific key value from my dictionary i can use square brackets
print(max(students, key = lambda i : i.get('score'))['name'])


students2 = {
    'manan' : {'age' : 14, 'score' : 100},
    'harshit' : {'age' : 14, 'score' : 95},
    'rohan' : {'age' : 14, 'score' : 98.8}
}
'''
what i want is 
to print the key value pair in which score is the highest
'''
print(max(students2, key = lambda i : students2[i]['score']))
'''
what i just did is
when i used lambda the variable i is the key actually 
so i accessed key from students2 and then in the key we have a dictionary so i accessed the key again
'''
