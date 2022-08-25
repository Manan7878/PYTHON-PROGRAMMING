'''we can also use all types of parameters in a single function'''

def func(name, *args , full_name = 'unknown', **kwargs): # order should always be the same if you change the order it will give you error
    print(name)
    print(args)
    print(full_name)
    print(kwargs)


func('manan', 1,2,3,a = 'abcd' )#if i don't pass argument for full name it will be default unknown
'''
so in the name parameter manan string will go
in args the integers i passed will go
even if i don't pass the argument for full_name it has a default value unknown
and in kwargs i passed a key value pair
'''


'''
if you don't want to use args and kwargs and only the default parameters the order should be : 
def func(name, full_name = 'unknown'
'''

# the oreder should be always like :        def func(name, *args , full_name = 'unknown', **kwargs): 
# to remember it yo u shuld use PADK = PARAMETER , ARGS , DEFAULT PARAMETER , KWARGS
