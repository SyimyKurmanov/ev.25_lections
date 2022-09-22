#Типы данных в питоне

#1. NoneType - Ничего, пустота -> None 
#2. BooLean - Истина или ложь -> True/False
#3. str() - Строки  -> "Hello world", 'My name is John'
#4. Числовые типы данных:
      #a. integer - int() - Целое число(-1, -2, 0, 1)
      #b. float() - Число с плавающей точкой (-1.2, 10,15)
      #c. complex()- Комплексные числа (3+5i6)
#5. Списковые типы данных: 
    #a. list(список/массив) -> [1, 2, 3, None, 'hello world', true, false, [1, 2, 3]]
    #b. tuple(кортеж) -> (1, 2 ,3, 4, None)    
    #c. range(последовательность) -> range(1, 10)
#6. set() ->   Множества
#7. dict(словари) -> содержит данные в виде ключа и значения -> {1: 'One', 2: 'Two'}
#************************************
#Mutable(изменяемые типы данных) 
       #1.list
       #2.set
       #3.dict
#Immitable (неизменяемые типы данных)
      #1. NoneType
      #2. boolean
      #3. int float complex
      # 4. str 
       #5. range
       #6. tuple
       #7. frozenset
       #********************************        
         

# '''Стандартный вывод данных '''
# """ 
# В пайтоне для вывода данных в терминал используется встроенная функция print() 
#   """
# print('Hello world! my name is Syimyk')
# print(27+5)

'''Стандартный ввод данных через терминал используется функция input()
  '''
a = input(' введите число: ')
print('В a хранится:')
print(a)

# print(input('Введите свое имя'))
text = hello world\nmy name is john\nim the baddest mf\n20 years old
print(text)