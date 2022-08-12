# step argument is mostly used in string concatenation and range function
#   for i in range(1,11,2)      (the third argument in step argument)
#it is used for skipping numbers
# if we write 2 in step argument it will print every second number
# or we ca say it will skip 1 number 
# so, if we write 3 in it so it will skip 2 numbers


# for i in range(1,21,2):# so it will skip 1 number each time in range 21
#      print(i)


print('<------------------------------->')
# so if we write negative numbers in step arguments then you have to write the range reversed
for i in range(11,0,-1):
    print(i)
