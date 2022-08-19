user = {'name':'manan', 'age':14}

'''when the get method do not finds the key so it returns none nut if you want it to returnsomething else you can do that'''
# after typing the key type a coma and type the thing you want to be returned by the get method
print(user.get('abcd', 'not found !'))# so now it will return not found

'''what happens when you use same key for more than one time'''

a = {'a':'b','a':'c'}
'''the last time you typed the same key will overwrite the previous same keys'''
'''as you can see there are two a in the dictionary the last a will overwrite all the a'''
'''so now if i print my dictionary it will print{'a':'c'}'''