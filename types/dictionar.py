# dict() - Словарь -Ю упорядоченная коллекция элементов (python 3.7 -> ordered). Каждый элемент в словаре хранится в виде пары: {ключ: значение}

# ассоциативный массив, hash tables, object(js), structure == dictionary(py)

# ключами могут выступать только неизменяемые типы данных и в словае хранятся уникальные ключи. Тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
#     }

# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])

# a = dict()
# b = {}
# print(a, b)
# print(type(a))
# print(type(b))

# ls= [('key1', 'value1'), ('key2', 'value2')]
# dict_ = dict(ls)
# print(dict_)

# -----------------------------------------------

# print(dir(dict))
# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmil.com',
#     'role': 'admin',
# }

# print(user_info.items())
# print(user_info.keys())
# print(user_info.values())

# for value in user_info.values():
#     print(value)

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')

# ls = list(user_info.items())
# print(ls[0][1])

# изменения элементов в словаре

# dict_ = {'name': 'Jack', 'age': 24}

# print(dict_['name'])
# dict_['name'] = 'John'
# dict_['address'] = 'WinterFell'
# print(dict_)

# dict_.update({'name': 'John', 'address': 'WinterFell'})
# print(dict_)

# ----------------------------------------

# Создание - fromkeys

# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

# --------------------------
# get
# dict_ = {1: 'pizza', 2: 'burger', 3: 'steak'}
# print(dict_.get(1))
# print(dict_[2])

# setdefault - работает так же как и get, но если нет такого ключа, то он создает новую пару из этого ключа

# dct = {'name': 'Eddard', 'last_name': 'Stark', 'age': 28}
# print(dct)
# print(dct.setdefault('age', 38))
# print(dct)

# Удаление эдементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dct = {'name': 'John', 'last_name': 'Snow'}

# removed = dct.pop('address', 'Такого ключа нет!!')
# print(dct)
# print(removed)

# popitem() - удаляет последнюю пару
# dct = {'name': 'John', 'last_name': 'Snow'}
# removed = dct.popitem()
# print(dct)
# print(removed)


# a = {'seinen': 'vagabond', 'shonen': 'naruto', 'adventure': 'vinland saga'}
# print(a['seinen'])

# seasons = {'лето':'жара', 'осень':'дождь', 'весна':'дождь', 'зима': 'снег'} 
# removed = seasons.pop('лето')
# print(removed)
