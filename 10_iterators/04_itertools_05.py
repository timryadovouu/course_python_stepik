import itertools as it
from collections import namedtuple
"""===================================================SUMMARY======================================================="""
"""
1.порождающие данные 
2.фильтрующие данные 
3.преобразующие данные
4.группирующие данные 
5.объединяющие или разделяющие данные 
6.порождающие комбинаторные данные <-- про это в данном блоке
"""


def permutations():
    """
    Возвращает итератор, который содержит все перестановки из элементов переданного итерируемого объекта.
    Каждая перестановка заключена в кортеж нужной длины.
    permutations(iterable, r)
    iterable — итерируемый объект
    r — целое число, длина возвращаемых кортежей; по умолчанию имеет значение None
    """

    numbers = [1, 2, 3, 4]
    letters = 'abc'
    all_num_permutations = it.permutations(numbers, 2)
    all_let_permutations = it.permutations(letters)
    print(list(all_num_permutations))
    print(list(all_let_permutations))

def combinations():
    """
    Возвращает итератор, который содержит все сочетания из элементов переданного итерируемого объекта.
    Каждое сочетание заключено в кортеж нужной длины.
    combinations(iterable, r)
    iterable — итерируемый объект
    r — целое число, длина возвращаемых кортежей
    """

    numbers = [1, 2, 3, 4]

    print(list(it.combinations(numbers, r=1)))
    print(list(it.combinations(numbers, r=2)))
    print(list(it.combinations(numbers, r=3)))
    print(list(it.combinations(numbers, r=4)))
combinations()

def combinations_with_replacement():
    """
    Возвращает итератор, который содержит все сочетания из элементов переданного итерируемого объекта с повторами.
    Те, один элемент в одном сочетании может встречаться более одного раза.
    combinations_with_replacement(iterable, r)
    iterable — итерируемый объект
    r — целое число, длина возвращаемых кортежей
    """

    numbers = [1, 2, 3, 4]

    print(list(it.combinations_with_replacement(numbers, 1)))
    print(list(it.combinations_with_replacement(numbers, 2)))
    print(list(it.combinations_with_replacement(numbers, 3)))

def product():
    """
    Возвращает итератор, который содержит декартово произведение всех переданных итерируемых объектов.
    product(iterables, repeat)
    *iterables — итерируемые объекты
    repeat — целое число, количество повторов; по умолчанию имеет значение 11
    """
    numbers = [1, 2]
    letters = ['x', 'y', 'z']
    flags = [False, True]

    print(list(it.product(numbers, letters, repeat=1)))
    # print(list(it.product(letters, numbers)))
    # print(list(it.product(letters, numbers, flags)))

"""===================================================TASKS======================================================="""

def task_1():
    """
    Способы купить книгу за 100 баксов
    """
    wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    print(sum([len([item for item in set(it.combinations(wallet, r=r_i)) if sum(item)==100]) for r_i in range(1, 14)]))

def task_2():
    wallet = [100, 50, 20, 10, 5]
    print(sum([len([item for item in set(it.combinations_with_replacement(wallet, r=r_i)) if sum(item)==100]) for r_i in range(1, 21)]))

def task_3(weight):
    """weight - масса в граммах -- нужно собрать наибольшую ценность"""
    Item = namedtuple('Item', ['name', 'mass', 'price'])

    items = [Item('Обручальное кольцо', 7, 49_000),
             Item('Мобильный телефон', 200, 110_000),
             Item('Ноутбук', 2000, 150_000),
             Item('Ручка Паркер', 20, 37_000),
             Item('Статуэтка Оскар', 4000, 28_000),
             Item('Наушники', 150, 11_000),
             Item('Гитара', 1500, 32_000),
             Item('Золотая монета', 8, 140_000),
             Item('Фотоаппарат', 720, 79_000),
             Item('Лимитированные кроссовки', 300, 80_000)]
    if any([weight >= item.mass for item in items]) is False:
        print("Рюкзак собрать не удастся")
    else:
        arr = [[item for item in set(it.combinations(items, r=r_i)) if sum([i.mass for i in item]) <= weight] for r_i in range(1, len(items)+1)]
        pre_max_list = [max([tpl for tpl in lst], key=lambda t:sum(i.price for i in t)) for lst in arr if lst]
        max_suite = max(pre_max_list, key=lambda tpl: sum(i.price for i in tpl))
        print(*sorted(item.name for item in max_suite), sep="\n")


def clock():
    [print(*time, sep=' : ') for time in it.product(range(1), range(2), range(60))]

def cards():
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз')
    suits = ('треф', 'бубен', 'червей', 'пики')
    print(*it.product(ranks, suits))

def chess_ground():
    from string import ascii_lowercase
    from itertools import product

    letters = ascii_lowercase[:8]
    digits = [1, 2, 3, 4, 5, 6, 7, 8]
    [print(f"{pair[0]}{pair[1]}", end=" ") for pair in product(letters, digits)]


from itertools import product
def password_gen():
    iterator = (f"{tpl[0]}{tpl[1]}{tpl[2]}"for tpl in product(range(10), range(10), range(10)))
    yield from iterator

def number_system(n, m):
    """
    Программа должна сгенерировать в системе счисления nn все числа длины mm и вывести их в порядке возрастания через пробел.
    :param n: основание системы <=16
    :param m: длина генерируемых чисел
    """
    from string import ascii_uppercase
    data = [*range(10)] + list(ascii_uppercase)[:8]
    # iterator = ("".join(map(str, tpl)) for tpl in it.product(*[data[:n] for _ in range(m)]))
    iterator = ("".join(map(str, tpl)) for tpl in it.product(data[:n], repeat=m))
    yield from iterator