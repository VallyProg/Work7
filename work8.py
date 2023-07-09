# def word(words):
#     str = words.lower().split()
#     f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
#     tmp = f(str[0])
#     if all([f(i) == tmp for i in str]):
#         return 'Парам пам-пам'
#     return 'Пам парам'


# print(word("пара-ра-рам рам-пам-папам па-ра-па-дам "))


# print(word("А-ведь-он-худеть-не-станет,\
#  Если-конечно,-вовремя-подкрепиться - да"))



# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)