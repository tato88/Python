def decor(func):
    def inner(*args):
        print('*' * 20)
        func(args)
        print('*' * 20)

    return inner


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Pet:
    def __init__(self, animal, nickname):
        self.animal = animal
        self.nickname = nickname

    def __str__(self):
        return self.animal, self.nickname


class Zoo_club:
    club_list = {}

    def __add__(self, other):
        Zoo_club.club_list.update({f'{Person(other)}': []})

    def add_pet(self, master, animal, nickname):
        for i in Zoo_club.club_list:
            if i == master:
                Zoo_club.club_list[i].append(Pet(animal, nickname).__str__())

    def del_pet(self, master, nickname):
        for i in Zoo_club.club_list:
            if i == master:
                for j in Zoo_club.club_list[i]:
                    if j[1] == nickname:
                        Zoo_club.club_list[i].remove(j)

    def del_persone(self, name):
        Zoo_club.club_list.pop(name)

    def del_animal(self, animal):
        for i in Zoo_club.club_list:
            for j in Zoo_club.club_list[i]:
                if j[0] == animal:
                    Zoo_club.club_list[i].remove(j)

    @decor
    def show_club(self):
        print(Zoo_club.club_list)


# x = {
#     'Person.name': [('cat', 'igor'), ('dog', 'igor')],'Person.name1': ['dog', 'ospa']
# }


def zooclub():
    new_zooclub = Zoo_club()
    while True:
        print('1) додати учасника в клуб')
        print('2) додати тваринку до учасника клубу')
        print('3) видалити тваринку з власника ')
        print('4) видалити учасника клубу ')
        print('5) видалити конкретну тваринку з усіх власників')
        print('6) Show Zoo Club')
        move = input('DO: ')
        try:
            match move:
                case '1':
                    x = input('Name? ')
                    new_zooclub.__add__(x)
                case '2':
                    x = input('master? ')
                    y = input('animal? ')
                    z = input('nickname? ')
                    new_zooclub.add_pet(x, y, z)
                case '3':
                    x = input('master? ')
                    y = input('nickname? ')
                    new_zooclub.del_pet(x, y)
                case '4':
                    x = input('name? ')
                    new_zooclub.del_persone(x)
                case '5':
                    x = input('which animal you wanna delete from all masters? ')
                    new_zooclub.del_animal(x)
                case '6':
                    new_zooclub.show_club()
        except Exception as err:
            print(err)


zooclub()
