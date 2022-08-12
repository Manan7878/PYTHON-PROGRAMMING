# if you want to check two statements in a single line we can use and operator
name = 'abc'
age = 123
if age  == 123 and name =="abc":
    print('ok')
else:
    print ('not ok')
# if both the conditions are true then it will print the ok even a single statement is false it will print not ok



# if you want to check that even a single statement is true we use or operator
name2 = 'cba'
age2 = 321
if name2 =='acb' or age2 == 321:
    print('ok')
else:
    print('not ok')

# now even if a single condition is true it will print ok 
# if both the statements are false then it will print not ok
