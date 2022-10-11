# Циклы - это конструкция, при помощи которой можно организовать многократное исполнение определенного кода

# while <expression>:
#     <body>
# <else>:
#     <body>


# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!')

# print('Начало кода')

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' or name2.lower() != 'jamie':
#     name1 = input('enter the name 1: ')
#     name2 = input('enter the name 2: ')
#     i += 1
#     if i > 4:
#         print('цикл остановлен!!')
#         break
# else:
#     print('вы ввели правильное имя!')


# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None
# while username != admin[0] or password != admin[1]:
#     username = input('vvedite username: ')
#     password = input('vvedite password: ')
#     i -= 1
#     if i == 0:
#         print('vy zblokirovany na 5 minut!')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zashli v systemu!')

# --------------------------

# for <variable> in <iterable object>:
#     <body>
# ls = [0, 1 ,2 ,3, 4, 5]
# i = iter(ls)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# for x in 'privet':
#     print(x)

# -------------------------

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for x in ls:
#     print(f'Element: {x}')

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1


# --------------------------------------------------------

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('enter a word: ')


# while word not in secret_list:
#     print('Incorrect word! Try one more time!')
#     word = input('enter a word: ')

# print(f'You\'re welcome my dear friend, {word}!')

# ------------------------------------------------

# 1)
# steps = 8
# path = 'UDDDUDUU'
# res = 1
# 2)
steps = 9
path = 'UDDUUDDUU'
# res = 2

sea_level = 0
count_valley = 0
# for x in path:
#     if x == 'D':
#         if sea_level == 0:
#             count_valley += 1
#         sea_level -= 1
#     else:
#         sea_level += 1

# print(count_valley)



for x in path:
    if x == 'U':
        sea_level += 1
        if sea_level == 0:
            count_valley += 1 
    elif x == 'D':
        sea_level -= 1
        
print(count_valley)

   

