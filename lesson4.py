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
#
#     def __add__(self, other):
#         notes_list = open('notebook.txt', 'a')
#         notes_list.write(''.join(f'{other.name} - {other.price}\n'))
#         notes_list.close()
#
#     @decor
#     def show_all_notes(self):
#         notes_list = open('notebook.txt', 'r')
#         print(notes_list.readlines())
#         notes_list.close()
#
#     @decor
#     def total_price(self):
#         notes_list = open('notebook.txt', 'r')
#         prices_list = []
#         for i in notes_list.readlines():
#             if i != '\n':
#                 prices_list.append(int(i.split(' - ')[1]))
#         total = sum(prices_list)
#         print(f'total is: {total}')
#         notes_list.close()
#
#     @decor
#     def most_expensive(self):
#         notes_list = open('notebook.txt', 'r')
#         x = 0
#         p = ''
#         for i in notes_list.readlines():
#             if i != '\n':
#                 if int(i.split(' - ')[1]) > x:
#                     x = int(i.split(' - ')[1])
#                     p = i.split(' - ')[0]
#         print(f'Most expensive is: {p, x}')
#         notes_list.close()
#
#     @decor
#     def find_purchase(self):
#         notes_list = open('notebook.txt', 'r')
#         prices_list = []
#         search = input('What are you search?')
#         for i in notes_list.readlines():
#             if i != '\n':
#                 if search == i.split(' - ')[0]:
#                     print(i)
#         notes_list.close()
#
#     @decor
#     def clear_notebook(self):
#         notes_list = open('notebook.txt', 'w')
#         notes_list.write('')
#         notes_list.close()
#         print('Nootebook is clear')
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
#         print('99) Clear Notebook')
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
#                 case '99':
#                     new_notebook.clear_notebook()
#                 case '9':
#                     return
#
#         except Exception as err:
#             print(err)
#
#
# notebook()
