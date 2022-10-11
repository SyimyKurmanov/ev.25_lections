# Типы данных -> Числа int(), float()
# = -> оператор присваивания
# number = 5
# print(number)
# tomorrow_day -> snake case 
# tomorrowDay -> Camel case 
# abc -> нижний регистр
# ABC -> верхний регистр
# + 
# num1 = 5
# num2 = 15
# result = a + b 
# print(result)
# print('результат суммы 5 и 15:',5+15)
# a = 100
# b = 1000
# c = 500 #int
# d = 56.20 #float
# print(a+b+c+d)
# - 
# num1 = 996
# num2 = 67.55
# print(num2-num1)

# * 
# num1 = int (input('введите число 1:'))
# num2 = int (input('введите число 2:'))
# result = num1*num2
# print("результат умножения", num1, "и", num2, result)

# num1 = input('введите число')
# print(num1)
# print(type(num1))

# num = '15'  
# num = int(num) #'15' -> 15
# print(type(num))

# / and // and %
# / -> обычное деление
# // -> целочисленное деление(деление без остатка)
# % -> модульное деление (остаток от деленя)

# num1 = 5
# num2 = 2

# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)

# ** -> возведение в степень
# num1 = 5
# print(num1 ** 1000)

# pow(a,b, <mod>) -> функция возведения в числа а в степнь в

# print(pow(2, 5, 5)) #2 ** 5 % 5 -> 2

#divmod(a, b) -> она выводит два числа, первое число это результат целочисленного деления(//), а второе число это модульное деление(%) двух чисел

# res = divmod(4,5)
# print(res)

#round() -> функция округления числа
# res = 24/13
# print(round(res, 3))

# abs() -> абсолютное значение = abs (-5) = 5 -> |-5| = 5

# print(abs(-101))
# print(abs(50))

# import math 
from math import pi, sqrt
# print(math.pi)

# math.sqrtm -> корень числа


# print(sqrt(25))
# print(sqrt(125))
# print(sqrt(100))
# print(pi)

# import math

# dir() - возвращает методы объекта или функции определнного модуля

# import math

# print(dir(math))

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1, num2)



# Инкремент и Дикремент

# Инкремент - увеличение значения какой-либо переменной. Пример: a = 1 (a += 1 -> a = a+1)
# a = 6
# # a += 5
# a += 1
# print(a)


# Дикремент - уменьшение значения какой-либо переменной. (a -= 1 -> a = a -1)

# a = 0
# a -= 1 
# print(a)


# # * 

# a = 5
# a *= a

# print(a)

# /
# a = 10
# a /= 2
# print(a)


# a = 7
# a %= 2
# print(a)

# id() -> номер в ячейке памяти

# a =1
# b = a
# print(id (a))
# print(id(b)) 


#  type() - выводит тип заданной переменной

# a = 9
# b = 'hello'

# print(type(a))
# print(type(b))


# var = int(input('type some shit'))


# a = int(input())
# b = int(input())
# print(total)

#  Модуль random - предоставляет функции для генерации случайных чисел, букв, символов

# import random
# print(dir(random))

# from random import choice

# from math import pi
# r = int(input('type radius:'))
# c = 2*pi*r
# s = pi*r**2
# print('длина окружности с радиусом 8, равна:', round(c))
# print('площадь круга с радиусом 8, равна:', round (s)) 


