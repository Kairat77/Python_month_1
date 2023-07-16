
# lst1 = [1, 2, 3, 4, 1, 3, 5]
# lst2 = {1, 2, 3, 4, 1, 3, 5}
# print(lst1)
# print(lst2)

# plov = {'carrot', 'rice', 'meat'}
# shorpo = {'meat', 'potato', 'water'}
# print(plov.difference(shorpo))


# print(plov.union(shorpo))
# print(plov.intersection(shorpo))
# print(plov.symmetric_difference(shorpo))


word = 'python'
while True:
    input_word = input('enter word:')
    if input_word == word:
        print('ok,' , word)
    elif set(input_word).issubset(word):
        print(f' no {input_word} there, maybe you mean,', word)
    else:
        print('no') 






# new = dict('python')

# new = dict([['1kairat','hello'], [2, 'bye']])
# print(new)



# student = {
#     'name': 'Kairat',
#     'age': 19,
#     'height': 2.60,
#     'married': False,
#     # list
#     'hobby': ['basketball', 'chess', 'english', 'books'], 

#     'education': ('scholl', 'college', 'kyrgyz course')
# }

# for i in student:
#     print(i, ':', student[i])


# for k, v in student.items():
#     print(k, ':',v)


# data = {}
# for i in range(1, 8):
#     data[f'day {i}'] = int(input(f'expense in day {i}:'))
# print(data)
# print(sum(data.values()) / len(data))

# data = {i: int(input(f'expense in day {i}:')) for i in range(1,8)}
# print(data, '\n', sum(data.values()) / len(data))


# print(student['name'])
# student['surname'] = 'Asanov'
# student.update(new)
'''edit'''
# student['hobby'][0] = 'footbal'
# student['education'] = list(student['education'])

'''delete'''
# deleted = student.pop('married')
# print(deleted)


# print(student['name'])
