import itertools as it
"""===================================================SUMMARY======================================================="""
"""
1.порождающие данные 
2.фильтрующие данные <-- про это в данном блоке
3.преобразующие данные
4.группирующие данные
5.объединяющие или разделяющие данные
6.порождающие комбинаторные данные
"""

def dropwhile():
    """
    Возвращает итератор, который генерирует элементы из входного итерируемого объекта сразу же после того,
    как для заданного условия будет получено ложное значение.
    dropwhile (predicate, iterable)
    predicate — фильтрующая функция, возвращающая bool значение
    iterable — итерируемый объект
    """
    numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

    new_numbers = list(it.dropwhile(lambda num: num <= 5, numbers))
    print(new_numbers)   #[6, 7, 8, 9, 10, 1, 2, 3]

    for word in it.dropwhile(lambda s: len(s) == 2, words):
        print(word, end=" __ ")        #python __ C# __ beegeek __ is __
def takewhile():
    """
    Возвращает итератор, который генерирует элементы из входного итерируемого объекта до тех пор,
    пока для заданного условия не будет получено ложное значение, те противоположность dropwhile()
    dropwhile(predicate, iterable)
    predicate — фильтрующая функция, возвращающая bool значение
    iterable — итерируемый объект
    """

    numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

    new_numbers = list(it.takewhile(lambda num: num <= 5, numbers))
    print(new_numbers)  #[1, 1, 2, 3, 4, 4, 5]

    for word in it.takewhile(lambda s: len(s) == 2, words):
        print(word, end=" __ ")   #is __ an __ of __


def filterfalse():
    """
    Возвращает итератор из элементов входного итерируемого объекта, для которых заданное условие ложно
    Противоположность filter()
    filterfalse(predicate, iterable)
    predicate — фильтрующая функция, возвращающая bool значение
    iterable — итерируемый объект
    Если predicate=None, то фильтрующая функция равнозначна функции bool()
    """
    numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

    new_numbers = list(it.filterfalse(lambda num: num <= 5, numbers))
    print(new_numbers)   #[6, 7, 8, 9, 10]

    for word in it.filterfalse(lambda s: len(s) == 2, words):
        print(word, end=" __ ")   #python __ beegeek __

def compress():
    """
    compress(iterable, selectors)
    iterable — итерируемый объект
    selectors — итерируемый объект, состоящий из значений True, False, который предоставляет значения, указывающие на то,
    какие входные значения следует брать, а какие следует игнорировать
    """
    data = 'ABCDEF'
    selectors = [True, False, True, False, True, False]
    result = it.compress(data, selectors)
    print(list(result))                     #['A', 'C', 'E']

def islice():
    """
    Возвращает итератор, который генерирует последовательность из выбранных элементов переданного итерируемого объекта
    islice(iterable, start, stop, step)
    iterable — итерируемый объект
    start — начало среза, default =  0
    stop — конец среза (не включительно)
    step — шаг среза, default = 1
    не поддерживает отрицательные значения
    """
    print(*it.islice(range(10), None))      # 0 1 2 3 4 5 6 7 8 9
    print(*it.islice(range(100), 5))     # 0 1 2 3 4
    print(*it.islice(range(100), 5, 10))     # 5 6 7 8 9
    print(*it.islice(range(100), 0, 100, 10))    # 0 10 20 30 40 50 60 70 80 90

"""===================================================TASKS======================================================="""

def drop_while_negative(iterable):
    yield from it.dropwhile(lambda num: num < 0, iterable)

def drop_this(iterable, obj):
    yield from it.dropwhile(lambda num: num==obj, iterable)

def first_true(iterable, predicate=None):
    return next(filter(predicate, iterable), None)


def take(iterable, n):
    # from itertools import islice as take
    yield from it.islice(iterable, n)

def take_nth(iterable, n):
    return next(it.islice(iterable, n-1, n), None)

def first_largest(iterable, number):
    # for index, item in enumerate(iterable):
    #     if item > number:
    #         return index
    # return -1
    yield next(it.compress(it.count(), (i>number for i in iterable)), -1)