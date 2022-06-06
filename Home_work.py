# написать блок- схему с помощью elif name= анна nomber 13 print(hi фттф)
# если name != Анна
# число угадано
# Программа если возвраст меньше 18 доступ запрещен
# если равен мы подумаем
# если больше 18 то проходите

name = "Анна"
number = 13
if name == "Анна":
    print("Привет, Анна")
elif number == 13:
    print("вы угадали")
else:
    print("не угадали")

    name = input()
    number = input()
    if name == "Анна":
        print("Привет, Анна")
    elif number == 13:
        print("вы угадали")
    else:
        print("не угадали")

a = int(input("введите ваш возвраст"))
if a == 18:
    print("мы подумаем")
elif a > 18:
    print("Проходите")
if a < 18:
    print("Проход закрыт")
