# работа с файлами
# режимы:
# w - write
# a - add
# x - создаст новый файл
# r - read
# file = open('file.txt', 'w')
# file.write('бишкек, Кыргызстан')
# file.close()

with open('file.txt', 'a') as file:
    file.write('22222222')