'''
we use def to define function
now make a function to add two numbers
'''

def add_two(a,b):
    return(a+b)
#so now this function is named  as add_two and this will take two integersand return the addition of the two numbers
# we can store them in a string and then print them

sum1 = add_two(123,456)
print(sum1)
# so here i recalled my function and stored it in a string named sum1 and printed it


# or if you have to do it more shortly you can use print dirctly instead of return


def add_3(a,b,c):
    print(a+b+c)

add_3(1,2,3)




# or there is one more way let's recall the first function we made and directly print it
print(add_two(1,1000))
