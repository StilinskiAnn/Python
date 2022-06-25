# a = True
# print(a)
#
# def big_data():
#     big_list = [1, 2, 3, 4, 5]
#     get_list(big_list)
# def get_list(list):
#     for vellyou in list:
#         print(vellyou)
# print(big_data())
#
# def main():
#     mt_list = []
#     trigger = "4"
#     while trigger == "4":
#         name = input("1")
#         mt_list.append(name)
#         trigger = input("а")
#         print(mt_list)
# main()

# def main():
#     name = ["book", "python", "dance"]
#     item = input(1)

#     try:                                #try- это обработка исключений
#         # get_index = name.index(item)
#         new_item = input(2)
#         new_item2 = input(2)
#         delenie = new_item / new_item2
#         print(delenie)
#         # name[get_index]= new_item
#     except:
#         print("error")
# # main()
#
# def main():
#     color = ["blue", "black", "pink"]
#     new_wall = int(input(2))
#     new_wall2 = input(3)
#     color.insert(new_wall, new_wall2)    #insert - добавляет
#     print(color)
# main()

# my_number = [4, 6, 9, 5, 7]
# my_number.sort() #Void функция возвращает None
# print(my_number)
#
# def main():
#     name =[1, 2, 3, 4]
#     word = int(input(1))
#     name.remove(word)
#     name.reverse()
#     print(max(name))
# # main()
#
# people_job = 5

# def main():
#     hour = [0] * people_job
#     for item in range(people_job):
#         hour[item] = float(input())
#     many_in_over = float(input())
#     for item in range(people_job):
#         big_money = hour[item] * many_in_over
#         print(big_money)
# main()
# проработать с методами и кортежами и строками то что сегодня и степик.

# def main():
#     big_list = []
#     item = int(input(1))
#     item2 = int(input(2))
#
#     big_list.insert(item, item2)
#     print(big_list)
# main()

# name = input().split()
# def spisok(dyda_petya, tetya_motya):
#     list = [[]]
#
#     for num in range(len(dyda_petya)):
#      list.append(dyda_petya)
#     return list
#
#
#
# print(spisok(name, "позиционный аргумент"))

# def main():
#     n = int(input(0))
#     m = int(input(8))
#     a = []
#     for i in range(n):
#         a.append([1] * m)
#         print(a)
# main()

name = input().split()
def spisok(dyda_petya, tetya_motya):
    list = [[]]

    for num in range(len(dyda_petya)):
        for num2 in range(num):
            list.append(dyda_petya[num2:num])
    return list


for num2 in range(2):
    print(num2)

# инкапсуляция - это абстракция которая защищает,скрывает функцию от внешнего воздействия

print(spisok(name, "позиционный аргумент"))

def main():
    def main2():
        print("hello Anna")

# рекурсия дз, бинарный поиск

my_list = []

while True:
    m = int(input(0))
    my_list.append(m)
    print(my_list)