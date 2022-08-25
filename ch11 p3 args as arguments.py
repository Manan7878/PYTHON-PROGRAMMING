def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

nums = [1,2,3]
# if you want to add nums from the list we have to use args as a argument
print(multiply_nums(*nums))# after the args type the name of your list 
'''what exactly it do is unpacking the list elements'''

# if it is a tuple it will work the same

# args is also a parameter but the things we typed like in the previous file : abcd (they are normal parameters)

