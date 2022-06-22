import json
from typing import TypedDict


def decor(func):
    def inner(*args):
        print('*' * 20)
        func(args)
        print('*' * 20)

    return inner


ZooType = TypedDict('ZooType', {'persone': str, 'Pets': list})


class ZooClub:
    def __init__(self, file_name):
        self.file_name = file_name
        self.club_list: list[ZooType] = []
        try:
            with open(file_name) as file:
                self.club_list: list[ZooType] = json.load(file)
        except:
            pass

    def add_persone(self):
        with open(self.file_name, 'w') as file:
            persone = input('name? ')
        self.club_list.append({'persone': persone, 'Pets': []})
        json.dump(self.club_list, file)

    @decor
    def show_all(self):
        if not self.club_list:
            print('there is no members')
            return
        for item in self.club_list:
            print(item)


zooclub = ZooClub('zooclub.json')

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
            case '6':
                zooclub.show_all()

    except Exception as err:
        print(err)
