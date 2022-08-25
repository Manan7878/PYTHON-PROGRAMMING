'''as previous we studied star operator args'''
'''now we will study double star known as kwargs'''
'''kwargs stands for keyword arguments'''
'''now i will define a simple function'''

def func(**kwargs):
    print(kwargs)

func(first_name = 'manan', last_name = 'sharma')
'''so now just like args you can pass infinite arguments'''
'''this actually creates dictionary'''
'''
args give the output in tuple
kwargs give the output in dictionaries
'''


'''now let's run a for loop in it'''
def func2(**kwargs2):
    for a, b in kwargs2.items():
        print(f'{a} : {b}')

func2(name = 'manan', last_name = 'sharma', age = 14)
'''so it will print key value pair'''


'''always remember when you use normal parameter with kwargs  so in its place do not enter a key value pair instead of it pass string'''


'''now let's talk about dictionary unpacking'''
d = {'name' : 'manan', 'age' : 14}
# you can also directly enter the already made dictionary into a argument 
'''
if you just enter d so it will give error
but if you type **d then it will work
'''

func2(**d)

