import copy
import random
from typing import List


def easy_way(people: List, n: int):
    teams: List[List] = list()
    for i in range(n):
        teams.append(list())
    for i in range(len(people)):
        teams[i % n].append(people[i])
    return teams


def hard_way(people, n):
    teams: List[List] = list()
    z = 5
    for i in range(z):
        teams.append(list())
    for i in range(len(people)):
        if i > ((5*n)-1):
            z = 4
        teams[i % z].append(people[i])
    return teams


def make_teams(people: List):
    a = len(people)
    if a <= 6:
        if a % 3 == 0:
            result = easy_way(people, 3)
        else:
            result = easy_way(people, a)
    elif a % 5 == 0 or a % 5 == 4:
        result = easy_way(people,5)
    elif a % 4 == 0 or a % 4 == 3:
        result = easy_way(people,4)
    elif a % 4 == 1:
        result = hard_way(people, 1)
    elif a % 4 == 2 and a > 10:
        result = hard_way(people, 2)
    else:
        result = None
    return result


def make_rooms(teams: List[List]):
    rooms: List[List] = list()
    a = len(teams[0])
    for i in range(a):
        rooms.append(list())
    for i in range(len(teams)):
        for j in range(len(teams[i])):
            rooms[j].append(teams[i][j])
    return rooms


def get_rooms(data: List, no_shuffle: bool = True):
    """
    Функция разбивающая по возможности список на группы по 4-5 элементов. Внутренняя логика немного запутанная,
    в следующих обновлениях перепишу.

    Пример:
        Входные данные:
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']

        Результат:
            [['N', 'B', 'J', 'Q', 'F'], ['D', 'L', 'I', 'R', 'P'], ['A', 'G', 'H', 'K'], ['C', 'O', 'M', 'E']]

        Результат с no_shuffle=True:
            [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J'], ['M', 'N', 'K', 'L'], ['Q', 'R', 'O', 'P']]
    :param data: Список чего угодно, что нужно распределить по комнатам/командам
    :param no_shuffle: Опциональный параметр, если False, состав комнат будет случаен, если нет, то в порядке из people
    :return: Список списков, где вложенный список - это состав комнаты
    """
    people = copy.deepcopy(data)
    if not no_shuffle:
        random.shuffle(people)
    return make_rooms(make_teams(people))


def test():
    people = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    data = people[:18]
    for i in range(3, 56):
        ...
        #data = people[:i]
        #data = list(range(i))
        #a = len(data)
        #print(data)
        #print(a)
        ##print(a, a%4, a%5)

        #teams = make_teams(data)
        #rooms = make_rooms(teams)

        #print(teams)
        #print(rooms)
    print(data)
    print(get_rooms(data=data, no_shuffle=False))
    print(get_rooms(data=data, no_shuffle=True))


if __name__ == "__main__":
    test()
