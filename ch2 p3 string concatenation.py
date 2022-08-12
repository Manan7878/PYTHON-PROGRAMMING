# strings
# anything inside double or single quotes
name = 'Manan'
surname = 'Sharma'

# string concatenation means joining strings
# we can use '+' sign 
fullname = name + ' ' + surname
print(fullname)
# we cannot join a string with integer or an float value
'''
print(fullname + 3)
        or
print(fullname + 4.2)
so you will get a error
'''
# but if you still want to cocatenate an string with a number you can write number as a string 
print(fullname + '4.2')# so now there will be no error

# or you can use string function to convert a value into string
print(fullname + str(4.2))

# but we can use multiplication in string with number
print(name *2)# so it will print the name 2 times



