# to check more than one conditions we use elif statement
# elif is used between if and else statements
age = input(int('enter yor age please : '))
if age == 0:
    print('sorry!! you cannot wach the film')
elif 0<age<10:
    print('price of the film ticket is 100')
elif 10<age<18:
    print('price of the film ticket is 150')
elif 18<age<50:
    print('price of the film ticket is125')
elif 50<age<80:
    print('price of the film ticket is 75')
else:
    print('you are are free to come in!!')


