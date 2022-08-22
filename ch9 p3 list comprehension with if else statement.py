nums = list(range(1,11))

'''
now what you have to do is create a list with range 1 to 10
in which if the number is even so multiply it with 2 
if the number is odd make it negative
'''

# normal way 
nums2 = []
for i in nums:
    if i%2==0:
        nums2.append(i*2)
    else:
        nums2.append(-i)

# with list comprehensi
nums3 = [i*2 if (i%2==0) else -i for i in nums]
'''
first what we wanted to append with if statement
and then else statement
then the for loop
you may find it complicated but after practicing it it'll be easier for you
'''

'''
note :      when we use if we typed the if statement at last but when we use if with else so they have to be typed before the for loop
'''

