import itertools as it
"""===================================================SUMMARY======================================================="""
"""
1.порождающие данные 
2.фильтрующие данные 
3.преобразующие данные
4.группирующие данные
5.объединяющие или разделяющие данные <-- про это в данном блоке
6.порождающие комбинаторные данные
"""

def chain():
    """
    Возвращает итератор, который последовательно генерирует элементы всех переданных итерируемых объектов
    chain(*iterables)
    *iterables — итерируемые объекты

    """
    chain_iter1 = it.chain('ABC', 'DEF')
    print(*chain_iter1)    #A B C D E F

    chain_iter2 = it.chain(enumerate('ABC'))
    print(*chain_iter2)                  #(0, 'A') (1, 'B') (2, 'C')

    for i in it.chain([1, 2, 3], ['a', 'b', 'c'], ('Timur', 29, 'Male', 'Teacher')):
        print(i, end=' ')              #1 2 3 a b c Timur 29 Male Teacher

def chain_from_iterable():
    """
    Принимает в качестве аргумента итерируемый объект, содержащий другие итерируемые объекты и возвращает итератор,
    который генерирует элементы всех вложенных итерируемых объектов
    chain.from_iterable(iterable)
    iterable — итерируемый объект, содержащий другие итерируемые объекты
    """
    chain_iter1 = it.chain.from_iterable(['ABC', 'DEF'])  # передаем список
    print(*chain_iter1)          #A B C D E F

    chain_iter2 = it.chain.from_iterable(enumerate('ABC'))
    print(*chain_iter2)             #0 A 1 B 2 C

    for i in it.chain.from_iterable(['Timur', '29', 'Male', 'Teacher']):
        print(i, end=' ')        #T i m u r 2 9 M a l e T e a c h e r


def zip_longest():
    """
     Чтобы обеспечить обработку всех входных элементов, когда итерируемые объекты имеют разные длины
     zip_longest(*iterables, fillvalue)
     *iterables — итерируемые объекты
     fillvalue - заполнитель, по умолчанию имеет значение None
    """
    print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
    print(*it.zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))  # fillvalue=None
    print(*it.zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*'))
    print(*it.zip_longest(['a', 'b', 'c', 'd', 'e'], [1, 2, 3], fillvalue=777))

    # (1, 'a')(2, 'b')(3, 'c')
    # (1, 'a')(2, 'b')(3, 'c')(None, 'd')(None, 'e')
    # (1, 'a')(2, 'b')(3, 'c')('*', 'd')('*', 'e')
    # ('a', 1)('b', 2)('c', 3)('d', 777)('e', 777)

def tee():
    """
    Позволяет создать несколько независимых итераторов на основе одного и того же итерируемого объекта
    tee(iterable, n)
    iterable — итерируемый объект
    n — количество создаваемых итераторов, по умолчанию имеет значение 2
    """
    iter1, iter2 = it.tee([1, 'a', 2, 'b', 3, 'c'])  # по умолчанию n=2

    print(*iter1)       #1 a 2 b 3 c
    print(*iter2)       #1 a 2 b 3 c



def pairwise():
    """
    Возвращает итератор, содержащий последовательные перекрывающиеся пары в виде кортежей,
    взятые из исходного итерируемого объекта
    pairwise(iterable)
    iterable — итерируемый объект
    from python 3.10
    """
    print(*it.pairwise('ABCDEFG'))            #('A', 'B') ('B', 'C') ('C', 'D') ('D', 'E') ('E', 'F') ('F', 'G')
    print(*it.pairwise([1, 2, 3, 4, 5]))      #(1, 2) (2, 3) (3, 4) (4, 5)


"""===================================================TASKS======================================================="""

def sum_of_digits(iterable):
    return sum(map(int, it.chain.from_iterable(map(str, iterable))))

def is_rising(iterable):

    return all(map(lambda pair: pair[0] < pair[1], it.pairwise(iterable)))

def max_pair(iterable):
    return max(map(lambda pair: pair[0] + pair[1], it.pairwise(iterable)))

def grouper(iterable, n):
    new_list = [*iter(iterable)]
    yield from it.zip_longest(*[new_list[i::n] for i in range(n)])
    # yield from zip_longest(*([iter(iterable)] * n))
    # return zip_longest(*repeat(iter(iterable), n))
