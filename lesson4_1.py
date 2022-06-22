import json
from typing import TypedDict

ZooType = TypedDict('ZooType', {'persone': str, 'Pets': list})


class ZooClub:
    def __init__(self, file_name, name):
        self.name = name
        self.file_name = file_name
        self.club_list: list[ZooType] = []
        try:
            with open(file_name) as file:
                self.club_list: list[ZooType] = json.load(file)
        except:
            pass

    # 1
    def add_persone(self):
        try:
            with open(self.file_name, 'w') as file:
                persone = input('name? ')
                self.club_list.append({'persone': persone, 'Pets': []})
                json.dump(self.club_list, file)
        except:
            print('Щось пішло не так!!!')

    # 2
    def add_pet(self):
        if not self.club_list:
            print('there is no members')
            return
        print('Add pet for whom? ')
        for item in self.club_list:
            print(self.club_list.index(item) + 1, item['persone'])
        choice = input('What number of persone? ')
        add_pet_to_persone_animal = input('what kind of pet? ')
        add_pet_to_persone_nickname = input('nickname of pet? ')
        # перевірка введеного числа
        if int(choice) in range(len(self.club_list) + 1):
            for item in self.club_list:
                if int(choice) - 1 == self.club_list.index(item):
                    try:
                        with open(self.file_name, 'a') as file:
                            item['Pets'].append({f'{add_pet_to_persone_animal}': add_pet_to_persone_nickname})
                            json.dump(self.club_list, file)

                    except:
                        print('Щось пішло не так!!!2')

    # 3
    def del_pet(self):
        if not self.club_list:
            print('there is no members')
            return
        print('Delete pet for whom? ')
        for item in self.club_list:
            print(self.club_list.index(item) + 1, item['persone'])
        choice = input('What number of persone? ')
        # перевірка введеного числа
        if int(choice) in range(len(self.club_list) + 1):
            for item in self.club_list:
                # вибір потрібного персонажа
                if int(choice) == self.club_list.index(item) + 1:
                    for i in item['Pets']:
                        print(item['Pets'].index(i) + 1, i)
                    choice_to_del = input('Nubmer of pet? ')
                    # перебираємо петів
                    for i in item['Pets']:
                        # чи є співпадіння
                        if int(choice_to_del) - 1 == item['Pets'].index(i):
                            try:
                                with open(self.file_name, 'a') as file:
                                    item['Pets'].remove(i)
                                    json.dump(self.club_list, file)

                            except:
                                print('Щось пішло не так!!!3')

    # 4
    def delete_persone(self):
        try:
            with open(self.file_name, 'a') as file:
                delete_persone = input('name? ')
                for item in self.club_list:
                    if item['persone'] == delete_persone:
                        self.club_list.remove(item)
                        json.dump(self.club_list, file)
        except:
            print('Щось пішло не так!!!4')

    # 5
    def delete_kind_of_animal(self):
        delete_animal = input('what kind of animal you wanna delete from club? ')
        for item in self.club_list:
            for animal in item['Pets']:
                if delete_animal in animal:
                    try:
                        with open(self.file_name, 'a') as file:
                            item['Pets'].remove(animal)
                            json.dump(self.club_list, file)

                    except:
                        print('Щось пішло не так!!!5')

    # 6
    def show_all(self):
        print('Зооклуб ', self.name)
        if not self.club_list:
            print('there is no members')
            return
        for item in self.club_list:
            print(item)


zooclub = ZooClub('zooclub.json', input('Введіть назву клубу: '))

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
                zooclub.add_persone()
            case '2':
                zooclub.add_pet()
            case '3':
                zooclub.del_pet()
            case '4':
                zooclub.delete_persone()
            case '5':
                zooclub.delete_kind_of_animal()
            case '6':
                zooclub.show_all()

    except Exception as err:
        print(err)
