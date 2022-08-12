# in this file we will learn some more methods we can use in lists






'''
1st 
count method: it counts that the data you typed in the bracket occurs how many times in the list
'''
nums = [1,2,1,2,2,3,5,5,3,2]
print(nums.count(2))# it will print 4 because 2 occurs 4 times in the list
print('<---------->')






'''
2nd
sort method: it sorts out data in the list alphabatically and ascending order in numericles
'''
nums2 = [10,3,2,4,5,6,7,8,9,1]
nums2.sort()
print(nums2)# so it will print the list in ascending order, it is same with alphabets also
print('<---------->')






'''
3rd
sorted function:it works just like the sort method but it does not make changes in the actual list but if you want to print the list a sorted way
it's for that
'''
list2 = ['c', 'd', 'b', 'a']
print(sorted(list2))# so it will just print the list in that way but not make change in the actual list
print('<---------->')






'''
4th
clear method: it will delete all the elements present in the list
'''
fake = [1,2,3,4,5,6,7,8,9,19]
fake.clear()# it makes changes in the actual list and now the whole list is empty
print(fake)
print('<---------->')





'''
5th
copy method:it is used to make a list same as a list which is already made. So it is used to copy the whole list
'''
a = [1,2,3,4,5,6]
b = a.copy()# so we created a list b by copying the list a
