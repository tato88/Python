# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# string = input('string?')
# if string.isdigit():
#     print(string)
# else:
#     new_string = []
#     for i in string:
#         if i.isdigit():
#             new_string.append(i)
# print(new_string)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# string = 'as 23 fdfdg544 34'
# if string.isdigit():
#     print(string)
# else:
#     new_string = ''
#     for i in string:
#         if not i.isdigit():
#             new_string += ' '
#         elif i.isdigit():
#             new_string += i
# result = new_string.split(' ')
# print(result)
# final_string = ''
# for i in result:
#     if i.isdigit():
#         final_string += i + ', '
# print(final_string.strip(', '))

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# greeting = [i.title() for i in greeting]
# print(greeting)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# test_list = [i ** 2 for i in range(51) if i % 2 == 1]
# print(test_list)

# function
#
# - створити функцію яка виводить ліст

# def show_list(list):
#     print(list)
#
#
# test_list = [1, 2, 3]
# show_list(test_list)


# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def find_min(a, b, c):
#     return min(a, b, c)
#
#
# print(find_min(22, 3, 5))


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def find_max(a, b, c):
#     return max(a, b, c)
#
#
# print(find_max(22, 33, 12))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def find_min_max(*args):
#                                   # x = [i for i in args]
#     print(max([i for i in args])) #or print(max(x))
#     return min([i for i in args]) #or return(min(x))
#
# find_min_max(22,45,76)


# - створити функцію яка повертає найбільше число з ліста

# def find_max_from_list(list):
#     return max(list)
#
#
# print(find_max_from_list([1, 22, 3, 2]))

# - створити функцію яка повертає найменьше число з ліста

def find_min_from_list(list):
    print(min(list))
    return min(list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def list_sum(list):
#     return sum(list)
#
#     # OR:
#     #
#     # x = 0
#     # for i in list:
#     #     x+=i
#     # return x
#
#
# print(list_sum([1, 2, 3]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_list(list):
#     return sum(list) / len(list)
#
#
# print(avg_list([2, 3, 4]))

#
#
#
#
#
#
#
# #################################################################################################
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"


#   - найти min число в листе
# print(min(list))

#   - удалить все дубликаты в листе
# print(set(list))

# # OR:
# list1 = []
# for i in list:
#     if i not in list1:
#         list1.append(i)
# print(list1)

#   - заменить каждое четвертое значение на "Х"
# i = 3
# while i <= len(list):
#     list.pop(i)
#     list.insert(i, 'x')
#     i += 4
#
# print(list)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# def square(a, b):
#     i = 1
#     print('*' * a)
#     while i <= b:
#         print('*' + (' ' * (a - 2)) + '*')
#         i += 1
#     print('*' * a)
#
#
# square(12, 8)

# 3) вывести табличку умножения с помощью цикла while

# a = 1
# b = 1
#
# while a < 10:
#     while b < 10:
#         print(str(a * b) + '  ' if a * b > 9 else str(a * b) + '   ', end = '')
#         b += 1
#     print()
#     a += 1
#     b = 1

# 4) переделать первое задание под меню с помощью цикла


while True:
    list_1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print('(1) найти min число в листе')
    print('(2) удалить все дубликаты в листе')
    print('(3) заменить каждое четвертое значение на "Х"')
    print('(5) stop')
    choice = input('wich one?')
    if choice == '1':
        find_min_from_list(list_1)
    elif choice == '2':
        print(set(list_1))
    elif choice == '3':
        i = 3
        while i <= len(list_1):
            list_1.pop(i)
            list_1.insert(i, 'x')
            i += 4
        print(list_1)
    elif choice == '4':
        break
