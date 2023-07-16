# time = 'day'

# if time == 'morning':
#     print('good morning')
# elif time == 'day':
#     print('good afternoon')
# elif time == 'evening':
#     print('good evening')
# else:
#     print('Hello')
# -----------------------------------------------
# print(2 == 3)
# print(2 != 3)
# print(2 > 3)
# print(2 < 3)
# print(2 <= 3)
# print(2 >= 3)
# print(1 < 2 > 3)

# sfetofor = input('введите цвет:')
# if sfetofor == "red":
#     print('stop')
# elif sfetofor == 'yellow':
#     print('жди')
# elif sfetofor == 'green':
#     print('go')
# else:
#     print('hello')
# ------------------------------------------------



# age = int(input('ваш возраст'))
# limit = 18
# if age >= limit:
#     print('welcome')
# else:
#     print(f'возраст не подходит! вам после {limit - age} год будет 18')

# ----------------------------------------------------
attems = 5

while attems > 0:
    temperatura = input(f'введите температуру: {attems} попыток')
    if temperatura == 'exit':
        print('goodbye')
        break
    temperatura = int(temperatura)

    if temperatura <= 10:
        print('холодно')
    elif temperatura >= 11 and temperatura <= 20:
        print('прохладно')
    elif temperatura >= 21 and temperatura <= 27:
        print('тепло')
    else:
        print('жарко')
        attems-=1
        

# --------------------------------------------------------

# password = input('vvedite passwod:')

# if len(password) >=8 and len(password)<=18:
#     print('длина подходит')
#     if not password.isalnum():
#         print('надежный')
#     else:
#         print('пароль не надожный')
# else:
#     print('длина не подходит')

