# Множества в пайтон - это некий "контейнер", который содержит в себе уникальные элементы в не упорядоченном виде.

# {} !!
# a = {1: 'a'} - dictionary
# a = {1, 2, 3} - set


# set_ = {8,1,2,3,4,5,6,7,7,7,7,7}
# print(set_)
# print(type(set_))

# ls = [0, 1, 2, 'a', True, False, 'n', 'b']
# str1 = 'My name is John Snow'
# ls.extend(str1)
# print(ls)
# res = list(set(ls))
# print(res)

# set1 = {*ls}
# res = [*set1]

# print(set1)
# print(type(set1))

# print(res)
# print(type(res))

# a = {1, 2, 3 ,4 ,5, 6, 7}

# print(a)
# a.pop()
# print(a)

# remove/discard
# remove -> error
# discard -> None

# a.discard(9)
# print(a)

# a.remove(5)
# print(a)

# frozenset
# a = {1, 2, 3, 4 ,5}
# f_set = frozenset([1, 2, 3, 4, 5])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)
# print(dir(f_set))

# a = set('qwerty')
# b = frozenset('qwerty')
# a.add(1)
# print(a)
# b.add(1)
# print(b)

# frozenset - неизменяемый тип данных

# -----------------------------------------

# Составьте код которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона: 
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным.
# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента (не попадитесь на этом и предупредите о том, что «Требуется ввести реальный номер месяца»).

month = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'jun',
    7: 'jul',
    8: 'aug',
    9: 'sep',
    10: 'oct',
    11: 'nov',
    12: 'dec',
}

while True:
    number = input('vvedite nomer mesyaca: ')
    if number == 'john':
        break

    if not number.isdigit() :
        print('Требуется ввести реальный номер месяца!')
        continue
    number = int(number)

    if number not in range(1, 13):
        print('Требуется ввести реальный номер месяца!')
        continue

    if number in range(3, 6):
        print(f'Вы родились в {month[number]}. Птицы пели прекрасные песни.')
    elif number in range(6, 9):
        print(f'Вы родились в {month[number]}. Солнце светило ярче чем когда-либо.')
    elif number in range(9, 12):
        print(f'Вы родились в {month[number]}. Урожай был невероятным.')
    else:
        print(f'Вы родились в {month[number]}. Зa окном падал белый снег.')


