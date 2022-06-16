# # Создать класс Rectangle:
# # -конструктор принимает две стороны x,y
# # -описать арифметические методы:
# #   + сума площадей двух экземпляров класса
# #   - разница площадей
# #   == или площади равны
# #   != не равны
# #   >, < меньше или больше
# #   при вызове метода len() подсчитывать сумму сторон
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#         self.area = (x * y) / 2
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __gt__(self, other):
#         return self.area < other.area
#
#     def __len__(self):
#         return self.x + self.y
#
#
# r1 = Rectangle(5, 6)
# r2 = Rectangle(5, 4)
#
# print(r1 + r2)
# print(r1 - r2)
# print(r1 == r2)
# print(r1 != r2)
# print(r1 > r2)
# print(r1 < r2)
# print(len(r1))
# print(r1)


# #
# #   ###############################################################################
# #   ###############################################################################
# #   ###############################################################################


# # создать класс Human (name, age)
# # создать два класса Prince и Cinderella:
# # у золушки должно быть имя возраст и размер ноги
# # у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
# #
# # в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# # и метод класса который будет показывать это количество
#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.count += 1
#
#     def how_many_cinderellas(self):
#         print(Cinderella.count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe):
#         super().__init__(name, age)
#         self.shoe = shoe
#
#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if self.shoe == cinderella.size:
#                 print(cinderella.name, cinderella.age, cinderella.size)
#                 return
#
#
# prince_max = Prince('Max', 18, 47)
# cinderellas = [Cinderella('Ira', 22, 35), Cinderella('Orysia', 45, 47), Cinderella('Olya', 24, 38)]
#
# prince_max.find_cinderella(cinderellas)
#
# cinderellas[0].how_many_cinderellas()


# #
# #   ###############################################################################
# #   ###############################################################################
# #   ###############################################################################


# # Для тех кому скучно:
# # 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# # 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# # 3) Створити клас Main в якому буде:
# # - змінна класу printable_list яка буде зберігати книжки та журнали
# # - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# # - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# # - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# #
# # Приклад:
# #
# # Main.add(Magazine('Magazine1'))
# #     Main.add(Book('Book1'))
# #     Main.add(Magazine('Magazine3'))
# #     Main.add(Magazine('Magazine2'))
# #     Main.add(Book('Book2'))
# #
# #     Main.show_all_magazines()
# #     print('-' * 40)
# #     Main.show_all_books()
#
# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     @abstractmethod
#     def print(self):
#         pass
#
#
# class Book(Printable):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def print(self):
#         print(self.name)
#
#
# class Magazine(Printable):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def print(self):
#         print(self.name)
#
#
# class Main:
#     list_magazines = []
#     list_books = []
#
#     def add(self, element):
#         if element.__class__ == Book:
#             Main.list_books.append(element.name)
#         elif element.__class__ == Magazine:
#             Main.list_magazines.append(element.name)
#         else:
#             pass
#
#     def show_all_books(self):
#         print(Main.list_books)
#
#     def show_all_magazines(self):
#         print(Main.list_magazines)
#
#
# bazar = Main()
# book1 = Book('3ti@')
# book2 = Book('GP')
# book3 = Book('step')
# magazine1 = Magazine('Play Boy')
# magazine2 = Magazine('Cars')
#
# bazar.add(book1)
# bazar.add(magazine2)
# bazar.add(book2)
# bazar.add(book3)
# bazar.add(magazine1)
#
# bazar.show_all_books()
# print('-' * 40)
# bazar.show_all_magazines()
