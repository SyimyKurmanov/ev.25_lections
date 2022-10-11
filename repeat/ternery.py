

# if sentence[-1] == '?':
#     print('Предложение вопросительное')
# else:
#     print('Обычное предложение')

# sentence = input('enter a sentence: ')
# print('предложение вопросительное' if sentence[-1] == '?' else 'обычное предложение')


# -------------------------------------------------------
# Ternary operator(Тернарный оператор) - конструкция, которая аналогична по своим свойствам и действию конструкции if/else, но при этом записывается в одну  строчку кода

# <выражение если в условии True> if <условие> else <выражение если Else>

# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits
# symbols = digits + '-' 
# print(symbols)
# number = input('vvedite cifru: ')
# is_correct = True
# for i in number:
#     if i not in symbols:
#         is_correct = False

# if is_correct:
#     print('yes, number')
#     number = int(number)
#     print('your number: ', number)
#     result = number if number >= 0 else -number 
#     print(result)
# else:
#     print('Invalid values!')



# number = input('vvedite chislo: ')
# if number.isdigit():
#     number = int(number)
#     print('Да, число!')

# else:
#     print('Вы ввели не число!')

# import string #string.digits
from string import digits #digits
flag = True
symbols = digits +'-'+'.'
while flag: 
    is_correct_number = True
    num1 = input('vvedite pervoe chislo: ')
    if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
         print('вы ввели неправильное число')
         is_correct_number = False

    for x in num1: 
        if x not in symbols:
            print('вы ввели неправильное число')
            is_correct_number = False
            break 
    if not is_correct_number:
        continue 
    num2 = input('vvedite vtoroe chislo: ')
    if len(num2) <= 1 and (num2 == '.' or num2 == '-') or not num2:
         print('вы ввели неправильное число')
         is_correct_number = False

    for x in num2: 
        if x not in symbols:
            print('вы ввели неправильное число')
            is_correct_number = False
            break 
    if not is_correct_number:
        continue 
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    print(num1)
    print(num2)

    operator = input('vvedite operator(+, -, *, /): ')

    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Результат: {round(num1 - num2, 2)}')
    elif operator == '*':
        print(f'Результат: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'Результат: {num1 / num2}')   
    else:
        print('Вы ввели неправильный оперотор!')   
    
    choice = input('Хотите остановить(yes): ')
    if choice.lower() == 'yes':
        flag = False
        print('Пока!')








