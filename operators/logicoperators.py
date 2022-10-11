# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения
# <, >, ==(равно), <=, >=, !=(не равно) 

# 1 < 5 -> True
# 7 > 9 -> False

# num1 = 15
# num2 = 15
# print(num1 != num2)

# num1 = 20
# num2 = 17
# print(num1>=num2)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(stroka1 > stroka2)

#  H #72  < W #87

# print(ord('H'))
# print(ord('а'))

# print(chr(1080), chr(4985))
# print(ord(' '))


# stroka1 = 'hello  '
# stroka = 'world privet'

# print(len(stroka1) > len(stroka))

#  Условные операторы 

# if
# elif
# else

# if <condition>: 
#     <body if> #сработает если в выражении if приедт True 

# [elif] <condition> 
#           <body elif>
# [else]: 
#  <body else # срабатывает если во всех выше стоящих условиях пришло False

# string = input('enter smt: ')

# if string.lower() == 'hello' :
#     print('Hello stranger!')
# elif string.lower() == 'john' : 
#     print('welcome back John Snow! The king of North!')
# elif string.lower()  == 'abra-kadabra':
#     print('Sim Salamon Kadabra')
# else:
#     print('Совпадений не найдено!')
# print(string)


# email = input('enter email: ')
# password1 = input('enter pasword: ')

# if len(password1) < 8:
#     raise ValueError('password too short!')

# password2 = input('enter password confirmation: ')
# if password2 != password1:
#     raise ValueError('password didn\'t match!')
# else:
#     print('successfully signed up!')
   
# age = input('enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!')
# if age < 18:
#     print(f'access denied! come again after{18 - age} age!')
# else:
#     print('you can buy it!!')
# Логические операторы
# and -> логическое и
# or -> логическое или
# not -> логическое отрицание

# my_age = 20
# your_age  = 18
# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 20 or your_age == 19
# print(result)

# result = not my_age == 20
# print(result)

# user = 'John'
# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 8001

# # либо юзер гугла или гитхаба и либо возраст выше 21
# # либо деньги(8000)
# if (is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):
#     print(f'You can enter the system, Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')



# Операторы идентификации
# in -> проверяет наличие элементов внутри какого-либо итерируемого объекта(строки, списки и т.д.)
# is -> сравинивает ячейки памяти двух объектов
    # == -> сравнивает по значению
# is not -> отрицательное сравнение ячеек памяти.

# str1 = 'Hello world'
# print(str1)
# choice = input('enter the symbol: ')

# if choice not in str1:
#     print(f'The symbol: {choice} does not exist!')
# else:
#     print(f'The symbol: {choice} exists!')





















































