# in this file we will learn about escape sequences
# there are many escape sequences

# to use an escape sequence we use a backslash    \   

#1st (to print single quotes inside single quotes and double quotes inside double quotes)
print('hello\'hi\'world')
# same we can do with the double quotes
print("hello\"hi\"world")

#2nd(to print something in a new line)
print('Manan')
print('Sharma')# to do this we can use \n
print('Manan\nSharma')# everything written in the string after \n will shift to a new line

#3rd(to give a tab space)
print('ab\tcd')# so it will give a tab space between ab and cd

#4th(to print backslash in string)
print('aa\\bb')#to print 1 backslash write 2 backslashes, to print 2 backslashes write 4 backslashes, to print three backslash write six backslash
# but if we have to print backslash at last we will face a problem
'''
print('this is backslash\')
'''
# it is wrong because the python will think that we are trying to write backslash single quote and the sentence is not completed 
# so it will show error


# the right way is
print('backslash\\')# so now there is a backslash after backslash so python will now do not show error



# last escape sequence(to use a backspace)
print('abcde\b')# so now the character before the backslash b will be deleted
