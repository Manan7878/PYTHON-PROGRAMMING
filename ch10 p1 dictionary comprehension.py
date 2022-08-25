'''this is also just the same thing like list comprehension'''
'''but in this we have key and value pair'''
'''
let's take an exaple like creting a dictionary in which key are integers from 1 to 10 and the value will be its square
'''

square = {num:num**2 for num in range(1,11)}
'''
what we done is
first we typed what key value pair we wanted to append
then we ran the for loop
'''

'''
now let's do something interesting
we want to print something like       (square of 1 : 1)
'''

'''we can use f string also'''

square2 = {f"square of {num} is" : num**2 for num in range(1,11)}



'''
now let's make a string 
and count how many characters occur how many times in it
'''

string = 'manan'
char_count = {char : string.count(char) for char in string}

'''
what we done is first we typed the key and then what we want in our value is the count of elements
the we ran the for loop
'''
