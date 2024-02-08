import itertools as it
import fractions
import operator

"""===================================================SUMMARY======================================================="""
"""
1.порождающие данные  <-- про это в данном блоке
2.фильтрующие данные
3.преобразующие данные
4.группирующие данные
5.объединяющие или разделяющие данные
6.порождающие комбинаторные данные
"""

def count():
    """
    count(start, step)
    start — начало отсчета, по умолчанию имеет значение 0
    step — шаг, по умолчанию имеет значение 1
    """
    count1 = it.count()
    print(next(count1), next(count1), next(count1))
    for i in zip(it.count(10), ['a', 'b', 'c']):
        print(i)

    frac_iter = it.count(1, fractions.Fraction(1, 2))
    print(next(frac_iter), next(frac_iter), next(frac_iter), next(frac_iter), next(frac_iter))
    for index, number in enumerate(it.count(1.0, 0.5)):
        if index < 6:
            print(number, end="___")
        else:
            break

def cycle():
    """
    cycle(iterable)
    iterable - итерируемый объект
    """
    cycle_iter = it.cycle([0, 1])
    print(next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter))

    for index, char in enumerate(it.cycle('abcd')):
        if index < 7:
            print(char, end="___")
        else:
            break
    print()
    for i in zip(range(1, 8), it.cycle(['a', 'b', 'c'])):
        print(i)
def repeat():
    """
    repeat(obj, times)
    obj — любой Python объект
    times — количество повторений, по умолчанию имеет значение None
    """
    for i, s in zip(it.count(1), it.repeat('bee-and-geek', 5)):
        print(i, s)

    repeat_iter = it.repeat([1, 2, 3])
    print(next(repeat_iter))
    print(next(repeat_iter))
    print(next(repeat_iter))

    for a, b, c in map(lambda x, y: (x, y, x*y), it.repeat(2), range(5)):
        print(f"{a} * {b} = {c}")
def starmap():
    """
    starmap(func, iterable)
    func — произвольная функция
    iterable — итерируемый объект, элементами которого являются итерируемые объекты
    """
    persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
    pairs = [(1, 3), (2, 5), (6, 4)]
    points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

    full_names = list(it.starmap(lambda name, surname: f'{name} {surname}', persons))

    print(full_names)
    print(*it.starmap(lambda a, b: a + b, pairs))
    print(*it.starmap(lambda x, y, z: x * y * z, points))
def accumulate():
    """
    accumulate(iterable, func, initial)
    iterable — итерируемый объект
    func — функция, принимающая два аргумента, по умолчанию используется функция сложения operator.add
    initial — начальное значение, по умолчанию имеет значение None (+ 1 элемент в начало)
    """
    import operator

    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    print(list(it.accumulate(data, initial=100)))        #45
    print(list(it.accumulate(data, operator.mul)))
    print(list(it.accumulate(data, max)))
    print(list(it.accumulate(data, min)))


"""===================================================TASKS======================================================="""

def tabulate(func):
    # yield from (func(_) for _ in it.count(1))
    return map(func, it.count(1))

def factorials(n):
    yield from it.accumulate(range(1, n+1), operator.mul)

def alnum_sequence():
    letters =[chr(i).upper() for i in range(ord("a"), ord("z")+1)]
    generator = it.cycle(element for pair in zip(range(1, 27), letters) for element in pair)
    yield from generator


def roundrobin(*args):
    iterators = [iter(a) for a in args]
    while iterators:
        q = []
        for iterator in iterators:
            c = next(iterator, "None")
            if c != "None":
                yield c
                q.append(iterator)
        iterators = q

