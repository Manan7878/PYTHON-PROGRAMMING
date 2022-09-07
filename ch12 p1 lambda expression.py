'''now we will study lambda expression'''
# which is also known as anonymous function

'''lambda expression is an expression which is used to create functions without names'''

# an example
lambda a,b : a+b
# as we can see first we used lambda and then we entered the arguments which it will take and after the semi column we typed what output we wanted
'''so now this will take two arguments a and b and it returns a+b'''

# now let's talk how can we use it
# to use it we can store it in a variable
add = lambda a,b : a+b
print(add(2,3))# so the output will be 5



'''
usually we don't assign lambda in a variable it was just for the understanding
we use lambda with built in functions like map, reduce, filter etc.
'''


'''now let's make a function for multiplying two numbers'''
multiply = lambda a,b : a*b
print(multiply(2,3.143))# we can add floating values also like 3.143

