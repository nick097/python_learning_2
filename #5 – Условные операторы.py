# Что такое условные операторы?
# Они отвечают за изменение поведения программы в зависимости от входных параметров,
# определённых в проверке. Проще говоря: если будет число 1, то программа запустит скрипт one,
# а если число 2 – скрипт two. Внутри условных операторов могут быть другие такие же условия
# для уточнения полученных данных. В рамках одного оператора можно сразу проверить пару условий.
# Для того, чтобы проверить несколько условий нужно их разделить элементом and (логическое и).



# Пример создания условия:

a = 2
if a != 0 and a != 1:
	print ("Проверка сработала")
# На экране будет показана запись лишь в том случае,
# когда переменная «a» не будет равна значению 0 и значению 1.
# То есть обе проверки в операторе должны выдать результат – true.



# Есть возможность произвести проверку с помощью or - логическое или.
# При использовании данного оператора достаточным поводом для запуска сообщения
# «Заработало» станет соответствие хотя бы одного из условий.
# Пример:

a = 1.1
if a != 1.1 or a > 0:
	print ("Проверка сработала")
# Исходный код
#
# Условный оператор «if-else»
user_data = int(input("Введите число: "))

isHappy = True

if isHappy or user_data == 6:
    print("User is happy")
elif user_data == 5:
    print("Number is 5")
elif user_data == 7:
    print("Number is 7")
else:
    print("User is unhappy")

if user_data != 5:
    print("Мы на месте")
    if user_data > 6:
         print("Number is bigger than 5")
        
# Тернарный оператор
data = input()

number = 5 if data == "Five" else 0

# if data == "Five":
#     number = 5
# else:
#     number = 0

print(number)
