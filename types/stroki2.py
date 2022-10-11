# str1 = 'hello world! My name is John Snow'

# res = str1.replace('John Snow', 'Jamie Lannister')
# print(res)

# print(id('H'))
# print(id('H'))
# print(id('h'))

# strip() - Убирает пробельные символы в начале и конце строки

# rstrip, lstrip

# text = input('enter the text:')
# print(text)
# print(len(text))
# res = text.strip()

# print(res)
# print(len(res))

# text = '   hello world   '

# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit ->           проверяет
# isnumeric -> ->   состоит ли наша строка
# isdecimal ->       полностью из чисел

# text = '572777'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops! Invalid symbols!')


# text = '\u00396'
# print(text.isnumeric())
# print(text)

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латиницы и кириллицы

# str1 = '56a'
# print(str1.isalnum())

# str2 = '56_a'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов латиницы и кириллицы.
# text = 'helloworld'
# print(text.isalpha())

# islower()
# isupper()
# istitle()

# str1 = 'Is My Name'
# print(str1.istitle())

# index(value, [start], [end]) -> выводит индекс значения value которое мы передаем в нашей строке
# count(value, [start]) ->  считает количество вхождений value в нашу строку

# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))


# text = 'Hello world! my name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)


# text = 'oooHello world! myo name is John Snowooo'
# text = input('enter text: ')
# i = 0
# res = -1
# while i < text.count('o'): #4
#     res = text.index('o', res+1)
#     print(res)
#     i += 1 #инкремент


# find(value, [start], [end]) -> делает тоже самое что и index, но есть одно отличие, в том что если value нет в строке то возвращается индекс -1

# text = 'hello'
# print(text.find('l'))
# print(text.index('hi'))

# swapcase() -> переводит все символы в противоположный регистр

# upper() все символы в верхний регситр 
#  lower() все символы в нижний регистр


# text = 'hellO World, JoHN, SNow'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

#capitalize () -> переводит первую букву в верхний регистр

# name = input('enter your name: ').capitalize()
# print(f'hello! Mr/Mrs {name}!')

#title() -> переводит первые символы всех слов в верхний регистр


# text = 'john , jamie, samsa, osman, said'
# print(text.title())
# print(text.capitalize())

# name = input('Vvedite FIO')
# print(name.title())


# split(разделитель) -> дробит строку на несколько частей по разделителю, который находится в строке. Все части строки сохраняются в тип данных list


# text = 'let me speak my turkish story, you, fookin pitch' 
# ls = text.split(' ')
# print(ls)
# print(len(ls))



# 'разделитель'.join(iterable(list)) -> соединяет по разделителю строки, которые находятся в list


# res = '#'.join(ls)
# print(res)







# mark = int(input('enter a mark'))

# if mark >= 90:
#     print('Отлично, ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')

labels = ['Honda', 'Toyota', 'Cevrolet', 'Mercedes']
for x in labels:
    print(f'i like brand {x}')










