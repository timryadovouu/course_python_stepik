import sys
import random
'''===================================================SUMMARY======================================================='''

#Посмотреть список всех методов и атрибутов Python объекта можно с помощью встроенной функции dir()

def foo():
    pass

def filterfalse(predicate, iterable):
    if predicate is None: predicate = bool
    return filter(lambda item: not predicate(item), iterable)

def transpose(matrix):
    return [list(_) for _ in zip(*matrix)]
# transpose = lambda matrix: [list(_) for _ in zip(*matrix)]

def get_min_max(data):
    if not data:
        pass
    else:
        new_list = list(data)
        return new_list.index(min(new_list)), new_list.index(max(new_list))

def starmap(func, iterable):
    # print(*zip(*iterable))
    # print(*map(func, *iterable)) смотрим, что она делает
    print(*map(lambda item: func(*item), iterable))
    return map(func, *zip(*iterable))

# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
# print(*starmap(lambda x, y, z: x * y * z, points))
#
# import copy
# def get_min_max(iterable):
#     try:
#         C=copy.deepcopy(iterable)
#         return(min(C),max(iterable))
#     except:return None
def get_min_max(iterable):
    try:
        iterator = iter(iterable)
        start_point = next(iterator)
        minimum, maximum = start_point, start_point
        while True:
            try:
                item = next(iterator)
                if item > maximum:
                    maximum = item
                elif item < minimum:
                    minimum = item
            except StopIteration:
                break
        return minimum, maximum
    except:
        pass

def qwe():
    def test_iter():
        return random.choice(list(range(1, 6)))
    # test_iter = lambda : random.choice(list(range(1, 6)))
    random_iterator = iter(test_iter, 2)
    [print(num) for num in random_iterator]
    # [print(num) for num in iter(test_iter, 2)]

# def example():
#     with open('data.txt') as file:
#         for line in iter(file.readline, ''):    # читаем, пока не попадется пустая строка
            # Делаем что-то с line.

infinite_love = iter(lambda: "i love beegeek!", None)
# print(next(infinite_love))
# print(next(infinite_love))
# print(next(infinite_love))

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


def is_iterator(obj):
    # print(hasattr(obj, "__next__"))
    try:
        next(obj)
        return True
    except:
        return False


def random_numbers(left: int, right: int):
    qw = iter(lambda: random.choice(list(range(left, right+1))), None)
    return qw

# iterator = random_numbers(1, 1)
# print(next(iterator))
# print(next(iterator))

