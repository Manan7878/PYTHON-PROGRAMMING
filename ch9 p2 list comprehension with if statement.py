nums = [1,2,3,4,5,6,7,8,9,10]

'''now what we have to do is create a list which have all the even numbers present in numbers list'''

# normal way
nums2= []
for i in nums:
    if i%2==0:
        nums2.append(i)


# with list comprehension
even = [i for i in nums if i%2==0]
'''
firt we typed what we wanted to append
then the for loop
then the if statement
'''
# as you can see it is more easier and comfortable with list comprehension


'''now let's create for odd numbers'''
'''note :  if you don't have a list already you can use range function in comprehension too'''

odd_nums = [i for i in range(1,12) if i%2!=0]#  !=   is used for not equals 


