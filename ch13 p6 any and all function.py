nums1 = [2,4,6,8,10]
nums2 = [1,2,3,4,5,6]
'''
before learning any and all first what we have to do is
we want to check if all the numbers are even in the list nums1
'''
# with loop
evens = []
for i in nums1:
    if i%2==0:
        evens.append(True)# always remember true is a value in python and the t in it should always be capital
    else:
        evens.append(False)# false is also a value just like true and the f should always be capital 

print(evens)# you will get a list in which there are five values and all are true because every number in nums1 is even

l = [True, False, True]
# what all function do is that it checks that all values are true or false
print(all(l))
# all values are true so in output we will get true but even there is a single thing taht is false so it will give false in the output
'''this was just for understanding'''


l2 = [2,4,5,6,8,10]
'''now if we want to check that all numbers are even or not so we will use all function'''
print(all([True if (i%2==0) else False for i in l2]))
# it will give true in the output but if there was a single other number except for even so it would have given false



'''
now let's talk about any function
what any function do is check that even a single value is true 
so if a single value is true so it will give true
'''
print(any([True if (i%2==0) else False for i in l2]))
# it will give true because if a single value is true so it will give true as the  output


