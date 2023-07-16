# c=0
# while c<100:
#     c+=1
#     if c == 10:
#         break
#     print('hello')
# c = 0


# while c<100:
#     c+=1
#     if c % 2 == 0:
#         continue
#     print('hello', c)

# round = 10

# while round > 0:
#     print(f'round, {round}')
#     if round == 6:
#         break
#     round -= 1

# word = 'programming'

# for i in word:
#     if i == 'm':
#         continue
#     print(i, end='')

# symbols = '!@#$%^*()_+'
# objects = '2qaz#&?223kd5d4'

# for terpit in objects:
#     if terpit.isnumeric():
#         print(terpit,'num')
#     elif terpit.isalpha():
#         print(terpit, 'alfa' )
#     elif terpit in symbols:
#         print(terpit, ' symfol')
#     else:
#         print('underfind')


cash = 100
years = 5
percents = 0.1

for i in range(1, years+1):
    
    cash+=cash*percents
    print(cash)
