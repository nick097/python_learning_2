first_num = 23.2 # Тип данных float
first_num = "1" # Тип данных string


first_num = 23.2 # Тип данных float
first_num = "1" # Тип данных string
# При объединение нескольких переменных с разными типами данных программа спровоцирует ошибку.


# Пример:
#
# first_num = "IloveYou"
# second_num = 13
# res = first_num + second_num # Скрипт выдаст ошибку
# Всего в Python есть 4 базовых типа переменных:
# some = 1 Integer - целые числа;
# some = 1.12 Float - числа с плавающей точкой;
# some = "Привет" String - строки;
# some = True Boolean - тип данных принимающий либо False, либо True.
# Есть и другие типы, но мы будем их разбирать в последующих уроках.

# В одной строке можно создать сразу несколько переменных:
first = sec = third = 1 # Всем трём переменным будет присвоено значение 1
# first, sec, third = "Hi", 75, 23.1 # Поочередное присвоение значений

###########
# Переменные и работа с ними
number = 5 # int

digit = -4.54356876 # float
word = "Результат:" # string
boolean = True # or False bool
del number #  удаление переменной
str_num = '5' # string

# print(word + str(digit))

print(word + str(number + int(str_num)))

del number

number = 7
print("Результат:", number)

##############
# Получение данных

num1 = int(input("Введите первое число: "))

num2 = int(input("Введите второе число: "))

num1 *= 5  # данную переменную умножаем на 5(подобным образом можно +-/ **)

print("Result:", num1 + num2)
print("Result:", num1 - num2)
print("Result:", num1 / num2)
print("Result:", num1 * num2)
print("Result:", num1 ** num2)
print("Result:", num1 // num2)

word = "Hi"
print(word * 2)     #   умножение строки

word = True
