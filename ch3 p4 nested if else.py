# we can use if in a else statement also
winning_number = 27
user_input = input('enter your lucky number :')
user_input = int(user_input)
if user_input == winning_number:
    print('you won')
else:
    if user_input < winning_number:
        print("too low")
    else:
        print('too high')


