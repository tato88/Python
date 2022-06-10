# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> list:
#         nonlocal todo_list
#         todo_list.append(todo)
#         return todo_list
#
#     def get_all():
#         print(todo_list)
#
#     add_todo('wake up')
#     add_todo('go to work')
#     add_todo('have a diner')
#     add_todo('go home')
#     add_todo('go to sleep')
#     get_all()
#
#     return todo_list
#
#
# notebook()


# def sum_raz(a: int) -> int:
#     n: str = str(a)
#     summa: int = 0
#     for i in range(len(n)):
#         summa += int(n[i])
#     return summa
#
#
# print(sum_raz(123))


# def sum_raz(a: int) -> str:
#     n: str = str(a)
#     array: list = []
#     summa: str = ''
#
#     for i, v in enumerate(n):
#         x: str = v + '0' * ((len(n)) - (i + 1))
#         array.append(x)
#         if x != '0' and int(x) > 0:
#             summa += '+' + x
#     print(array)
#     return summa
#
#
# print(sum_raz(10800))


