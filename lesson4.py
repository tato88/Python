# # # есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com
#
# file = open('emails.txt', 'r')
# new_file = open('new_emails.txt', 'a')
# try:
#     for i in file.readlines():
#         mail = str(i).partition('			')[2].partition('@')[2].strip('\n')
#         if mail == 'gmail.com':
#             new_file.write(i)
# except Exception as err:
#     print(err)
# new_file.close()
# file.close()


##########################################################################################################
##########################################################################################################
##########################################################################################################


# # # 2) для хранения и чтения данных использовать файлы
# # #
# # # реализовать записную книжку покупок:
# # # - каждая запись должна содержать название покупки и ее цену
# # # -сделать менюшку для работы с записной книжкой:
# # #     '1) Создать запись'
# # #     '2) Список все записей'
# # #     '3) Общая сумма всех покупок'
# # #     '4) Самая дорогая покупка'
# # #     '5) Поиск по названию покупки'
# # #     '9) Выход'
# # # - можете придумать свои пункты
#
#
# def decor(func):
#     def inner(*args):
#         print('--------------------')
#         func(args)
#         print('--------------------')
#
#     return inner
#
#
# class Main:
#     notes_list = []
#
#     def __add__(self, other):
#         Main.notes_list.append((other.name, other.price))
#
#     @decor
#     def show_all_notes(self):
#         print(Main.notes_list)
#
#     @decor
#     def total_price(self):
#         prices_list = []
#         for i in Main.notes_list:
#             prices_list.append(int(i[1]))
#         total = sum(prices_list)
#         print(f'total is: {total}')
#
#     @decor
#     def most_expensive(self):
#         x = 0
#         p = ''
#         for i in Main.notes_list:
#             if int(i[1]) > x:
#                 x = int(i[1])
#                 p = i[0]
#         print(f'Most expensive is: {p, x}')
#
#     @decor
#     def find_purchase(self):
#         prices_list = []
#         search = input('What are you search?')
#         for i in Main.notes_list:
#             if search == i[0]:
#                 print(i)
#
#
# class Purchase:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return self.name, self.price
#
#
# def notebook():
#     new_notebook = Main()
#     while True:
#         print('1) ADD Purchase')
#         print('2) Show all Purchases')
#         print('3) Total Price')
#         print('4) Most expensive Purchase')
#         print('5) Find Purchase')
#         print('9) Exit')
#         move = input('DO: ')
#         try:
#             match move:
#                 case '1':
#                     x = input('Purchase? ')
#                     y = input('Price? ')
#                     new_notebook.__add__(Purchase(x, y))
#                 case '2':
#                     new_notebook.show_all_notes()
#                 case '3':
#                     new_notebook.total_price()
#                 case '4':
#                     new_notebook.most_expensive()
#                 case '5':
#                     new_notebook.find_purchase()
#                 case '9':
#                     return
#
#         except Exception as err:
#             print(err)
#
#
# notebook()
