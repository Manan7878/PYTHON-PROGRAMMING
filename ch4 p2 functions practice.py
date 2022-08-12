# in this file we'll do some more practice with functions
# so let's make a code that will print the last character ofthe string
def last_char(name):
    return name[-1]

print(last_char('abcd'))



print('<---------------------------------------------------------->')





# now let's make a function that will take number and in return it will tell us that the number is even or odd
def odd_even(num):
    if num%2 ==0:
        return 'even'
    else:
        return 'odd'
print(odd_even(111111111111111111111111111111111111111111111111111111111111111111111111111))


print('<----------------------------------------------------------------------->')


# now let us make a function that will tell us the greatest number among 3 numbers
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

print(greatest(1,27,3))

print('<------------------------------------------------------------------->')