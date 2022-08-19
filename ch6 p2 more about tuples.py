# we can use looping in tuples
abcd = (1,2,3,4.5)
for i in abcd:
    print(i)
# we can use while loop too


# tuple with one element
#  ab = (1)      this is not a tuple you can use type function to check
# ab = (1,2)    but this is
'''
to make tuple with only one element just type a coma after the element so python will know that it is a tuple
example = (1,)        so this is a tuple
'''



# tuple without parenthesis

names = 'manan', 'yukti'
# so by default it will be a tuple




#tuple unpacking
a = 'a', 'b', 'c'
name1, name2, name3 = a
# you have to use exactly the same numbers of elements presrent in the tuple
# so a is assigned to name1 b to name2 and c to name3





# list inside tuple
b = ('abcd', ['hello','world'])
#so now there are 4 elements in the tuple (1,2,3 and the list)
# so now i can add and delete data     but the only data related data to the list present in our tuple

# now let's try to pop something from the list
b[1].pop()# so now the element in the list which have the position 1 will be popped
print(b)
# we can also append


# we can use min(), max, sum also
nums = 1,3,5,7,9
print(sum(nums))