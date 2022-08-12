nums = [[1,2,3],[4,5,6],[7,8,9]]
# this is known as lists inside list
# this type of list is known as 2d list
# there are 3 items in the list as you can see
# if we print positon 1 it will print the list with 4,5,6



# now let's run a loop
for i in nums:
    print(i)
print('<---->')




for a in nums:
    for i in a:
        print(i)
'''
what this will do is 
first we use the loop and then we used loop inside a loop to print the items in the lists        
'''
print('<----->')


# so now I want to print a specific element from a specific list
print(nums[1][1])# so now it will print 5
print('<----->')




# now let's talk about type function 
# type has no relation with lists inside list
# it is used to check what kind of data is it

s = 'abcd'
print(type(s))# it will give a output class str
# so it means its a strings