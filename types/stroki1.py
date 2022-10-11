# String - тип данных строки

"hello world"
'hello world'

"""
hello world
i am student
"""

# a = 5 #comment - коммент

# Строки - это набор последовательных символов, которые мы используем для хранения и предстваления текстовой информации.
# Набор методов и операций, которые мы можем использовать с данными в виде текста.

# индексация в строке
# name = 'John'
#    J = 0 = -4
#    o = 1 = -3
#    h = 2 = -2
#    n = 3 = -1

# print(name)
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])

# print(str1[-3], str1[-2], str1[-1])

# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# # Срезы по индексам
# [start: end: <step>]
# str1 = 'birthday'
# str2 = str1[0: 5]
# print(str2)
# print(str1[5:8])
# print(len(str1))
# print(str1[5:]) #до конца

# text = 'hello world! my name is Syimyk! I\'m student!'
# print(text)
# print(len(text))

# print(text[:12])
# print(text[13:31])
# print(text[32:])
# print(text[:12:3])
# print(text[::2])
# print(text[::-1])
# print(text[:12:-1])

#Конкатенация строк(слияние, соединение)

# word1 = 'hello'
# word2 = 'world'
# probel = ' '
# result = word1 + probel + word2

# print(result)
# print(word1+ ' ' +word2 + '!!!')

# # форматирование строк
# 1. с помощью %
# 2. с помощью (.format())
# 3. Интерполяция строк (f-строки)

# %
# name = input('enter your name')
# last_name = input('enter your last name:')

# print('hello, my nmae is', name, last_name)
# print('hello, my name is' + ' ', + name +' '+ last_name)
# print('hello, my name is %s -> %s' %(name, last_name))

# .format
# name = input('enter your name:')
# last_name = input('enter your last name:')

# print('hello, my name is {} {}' .format(name, last_name))

# f-строки
# name = input('enter your name:')
# last_name = input('enter your last name:')

# print(f'hello, my name is {name} {last_name}!')

#Экранирование строк - механизм при помощи которого можно вставлять символы, которые сложно ввести с клавиатуры в строку


#  \n -перенос строки 
#  \t - горизонтальная табуляция
#  \v - вертикальная табуляция

# name = 'john \nsnow'
# lastName = '\vsnow'
# last_name= '\tSnow'

# print(name)
# print(lastName)
# print(last_name)






