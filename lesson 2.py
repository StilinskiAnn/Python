#Функция len() возвращает длину (количество элементов) в объекте.
#Аргумент может быть последовательностью, такой как строка, байты, кортеж, список или диапазон или коллекцией (такой как словарь, множество или неизменяемое множество).
#Когда объект является строкой, функция len() возвращает количество символов в строке.
# Round — встроенная функция Python. Ее задача — округлять число с плавающей точкой до той цифры, которую задает пользователь.
# Если ее не задать, то возвращается ближайшее целое число, ведь значением по умолчанию является 0. Функция round помогает «улучшать» числа с плавающей точкой.



#print('Как вас зовут?')
#name = input()
#print('Здравствуйте, ' + name + '!')

#a = int(input())
#b = int(input())
#c = a / b
#print(c)
#word = len("hello world")
#print(word)
# Булев тип данных True(истина) и False(ложь) (не заключается в кавычки  и начинаются с прописной)
chek = True
chek_1 = False
print(chek_1)
# операторы сравнения сопоставляют два значения и возращают результат в виде булева значения
# оператор     операция
# ==             равно
# !=             не равно
# <              меньше
# >              больше
# <=             меньше или равно
# >=             больше или равно
#булевы операторы
# and это и ,работают с двумя булевыми значекниями
# or  или (вернет True, когда один из операторов True)
# not не (применяется только к 1 булевому значению, унарный оператор)
# таблица истиности для оператора and
# Выражение         результат
# True and True     True
# True and False    False
# False and True    False
# False and False   False
# таблица истиности для оператора or
# Выражение         результат
# True or True       True
# True or False      True
# False or True      True
# False or False     False
# Таблица истинности для оператора not
# Выражение         результат
# not True            False
# not False           True
print(1 == 1)
print(1 != 1)
print(1 <= 1)
print(True != False)
print(1 == 1.0)
print(1 == "1.0")
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 2 ) or (2 == 2))
anna = True
if  not True:
    print("Bonjour Anna")
elif not anna:
    print("правда")
elif anna == True:
    print("правда2")
else:
    print("non")
 # elif инструкция переводиться как иначе-если , и содержит блок условий
name = "Анна"
number = 13
if name == "Анна" and number != 13:
    print("вы угадали")
else:
    print("Вы не угадали")