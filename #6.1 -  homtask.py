# 1 Работа с циклами
# Выведите столбец чисел от 34 до 67 с выводом только четных чисел.
#
# Используйте цикл while для этой задачи.

a = 34

while a<=67:
 if a % 2 !=1:
  print(a)
 a+=1

 ###############################################
 # 2 Вывод чисел Выведите числа от 1 до 100 с
 # пропуском чисел 50 и 99.
 # Создайте вывод при помощи цикла for , а также цикла while.

# вывод при помощи цикла for
for x in range(1, 100+1):
 if x ==58 or x ==99:
  continue
 print(x)

# вывод при помощи цикла while

a = 1
while a<=100:
 if a !=58 and a !=99:
  print(a)
 a +=1


 # if a ==58 or a ==99:
 #  continue

#################################
# 3 Небольшая игра
# Попросите пользователя ввести какое-либо слово, а также число.
# При помощи циклов выведите каждый символ строки, при этом символ должен повторяться количество раз равным числу, что ввел пользователь. Каждый последующий новый символ необходимо выводить с новой строки, например:
#
# Привет # То что ввел пользователь
# 3 # Число, которое ввел пользовать

# Результат
# ППП
# ррр
# иии
# ввв
# еее
# ттт


x = input("please enter word ")
y = int(input("please enter numder"))

for i in x:
 print(i * y)