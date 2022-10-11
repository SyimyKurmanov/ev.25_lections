# names = ['syimyk husein kurmanov', 'medina kuba', 'arlan isakov', 'jane austen', 'sherman alexie']
# res = []
# names = []
# for x in range(0, 5):
#     name  = input('enter a full name: ')
#     names.append(name)

# result = []
# for x in names:
#     x = x.split(' ')
#     print(x)
#     result.append(x[-1])

# result.sort()
# print(result)

# ----------------------------------------
# range(start, stop, [step])  - возвращает последовательность из целых чисел, начиная с start до stop, возвращает итерируемый тип данных range

# x = range(1, 101)
# print(list(x))
# print(x)
# for num in x:
#     print(num)

# res = 0
# for num in range(1, 101):
#     res += num
# print(res)




# /// TASK8 \\\
# Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
# Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Результат:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
# list1 = []

# for x in range(0, len(list_), n):
#     list1.append(list_[x])
#     # print(list_[x])

# print(list1)



# res = []
# for x in range(0, 3):
#     ls = []
#     for x in range(0, 3):
#         ls.append(0)
#     res.append(ls)

# print(res)

# /// TASK4 \\\
# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# list_ = [1, 2, 3]
# Результат:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1


from itertools import combinations, combinations_with_replacement, permutations
res = list(permutations([1, 2, 3], 3))
print(res)



