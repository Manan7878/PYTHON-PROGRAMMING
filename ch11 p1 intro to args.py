'''*args is used to make a function flexible'''
'''
what it means is if i define a function
def total(a, b):
    return a+b
so it will take two arguments
but if we want to add more arguments without changing the function like add more variables or something like that
so we use *args(pronounced as :   0 star args)
'''


def total(a, b):
    return a+b
'''now let me recall my function'''
'print(total(3,4))'# but if i pass more than two arguments so it will give me a error

'''that is what i mean to making functions flexible'''
'''this is why we use args'''

'''this is how we can use'''

def all_total(*args):
    print(args)


all_total(1,2,3)
'''
first of all you make sure that this work is done by star operator not by typing args
because some people think that args is a keyword
you can type anything in its place like :   num, nums, ab, a etc.
'''


'''
the type of output it gives is tuple
you can check by type function
'''

'''now let's make a function of addition  but in this function it will give us the sum of all numbers we pass'''

def total2(*args):
    add = 0
    for i in args:
        add += i
    return add
print(total2(1,2,3,4,5))

'''
what we done here is first we defined a function total2
we created an empty variable with value 0
every time the loop ran every passed argument got added in the variable
'''


