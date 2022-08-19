# first of all we will define a function which has two values
def func(int1 , int2):
    add = int1 + int2
    multiply = int1*int2
    return add , multiply

print(func(2,4))
# the output will be like this(6, 8) which is a tuple
# it means it is not giving you two values but it is just a single value
# but you can store them in two different variables 


add , multiply = func(3,5)
'''
the function we defined first returns us the add value and then the multiply value
so it means the first vale will be stored in the add variable and the second one in the multiply variable
'''
# now you can print by variables