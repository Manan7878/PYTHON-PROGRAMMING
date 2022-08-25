def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

'''
so now multiply_nums is a function with infinite arguments can be passed
we created a variable with value 1 because if we have put 0 in there so 0 multiplied by anything is 0
we ran for loop
and we returned multiply
'''



'''now let's talk about normal parameters'''

def add(nums, abc,  *args):# in this nums and abc are parameters
    a = 0
    for i in args:
        a+=i
    return a

print(add(1,2,3))
'''
the output will be 3 because if we type anything else except star there are two more things so the first two arguments will go to those parameters
'''

# note :    always remember if you have not typed any parameter and you pass no argument in the function so it will not give you error
#           but if you have typed a parameter and you pass no argument so it will give you error
#           so it means that in parameters there always have to be something for every parameter you have typed
#           for parameters you can also pass string in the argument
# note2 :    you cannot type parameter after args you have to type it before args


