import sys
import csv
from datetime import date
import calendar
'''===================================================SUMMARY======================================================='''
def summary():
    # генератор
    class GenerateInts:
        def __init__(self, n):
            self.n = n
            self.current = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.current == self.n:
                raise StopIteration
            else:
                self.current += 1
                return self.current - 1
    def generate_ints(n):
        for num in range(n):
            yield num

    generator1 = generate_ints(5)
    # print(next(generator1))
    # print(next(generator1)

    def example():
        def counter(low, high):
            for num in range(low, high + 1):
                yield num
        class Counter:
            def __init__(self, low, high):
                self.low = low
                self.high = high

            def __iter__(self):
                return self

            def __next__(self):
                if self.low > self.high:
                    raise StopIteration
                else:
                    self.low += 1
                    return self.low - 1

    def counter(low, high):
        for num in range(low, high + 1):
            yield num

'''===================================================TASKS======================================================='''

def simple_sequence():
    """1,2,2,3,3,3,4,4,4,4,.."""
    num = 1
    while True:
        for _ in range(num):
            yield num
        num += 1

def alternating_sequence(count = None):
    """1,−2,3,−4,5,−6,7,−8,9,−10,..."""
    start = 1
    if isinstance(count, int):
        for _ in range(count):
            yield ((-1)**_) * (_+1)
    else:
        while True:
            yield (-1)**(start+1) * start
            start += 1


def primes(left, right):
    for _ in range(left, right+1):
        counter= 0
        for k in range(1, _+1):
            if _%k == 0:
                counter +=1
        if counter == 2:
            yield _

from datetime import date, timedelta
def reverse(sequence):
    for _ in sequence[::-1]:
        yield _

def dates(start, count=None):
    if count:
        for _ in range(count):
            yield start
            start += timedelta(days=1)
    else:
        try:
            while True:
                yield start
                start += timedelta(days=1)
        except:
            pass

def card_deck(suit):
    """все кроме suit"""
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    mast = ["пик", "треф", "бубен", "червей"]
    del mast[mast.index(suit)]
    all_cards = [f"{c} {m}" for m in mast for c in cards]
    while True:
        for _ in all_cards:
            yield _

'''===================================================SUMMARY======================================================='''

def foo():
    """
    def get_data():
    for num in range(5):
        yield num
    for char in 'ABC':
        yield char
    """
    # is equal to
    def get_data():
        yield from range(5)
        yield from 'ABC'

'''===================================================TASKS======================================================='''

def matrix_by_elem(matrix):
    for line in matrix:
        yield from line


def palindromes(start=1):
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1

def flatten(nested_list):
    """Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list,те распаковка"""
    for item in nested_list:
        if isinstance(item, int):
            yield item
        else:
            yield from flatten(item)


# module_2 Генераторные выражения

def cubes_of_odds(iterable):
    return (item**3 for item in iterable if item%2!=0)

def is_prime(number):
    return sum(1 if number%item==0 else 0 for item in range(1, number+1)) == 2

def count_iterable(iterable):
    return sum(1 for _ in iterable)

def all_together(*args):
    """objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
    0 1 2 b e e 1 3 5 2 4 6"""
    return (item for iterable in args for item in iterable)
    # for _ in args:
    #     yield from _

def interleave(*args):
    """
    print(*interleave('bee', '123'))
    b 1 e 2 e 3
    """
    t = len(args[0])
    return (iterable[_] for _ in range(t) for iterable in args)

# module_3_1 Генераторные выражения

def first():
    from collections import namedtuple
    Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
    persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
               Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
               Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
               Person('Genevieve Asse', 'French', 'female', 1949, 0),
               Person('Irene Adler', 'Swedish', 'female', 2005, 0),
               Person('Sergio Asti', 'Italian', 'male', 1926, 0),
               Person('Olof Backman', 'Swedish', 'male', 1999, 0),
               Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
               Person('Dana Atchley', 'American', 'female', 1941, 2000),
               Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
               Person('Shura_Stone', 'Russian', 'male', 2000, 0),
               Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

    alive = (person for person in persons if not person.death)
    swed = (person for person in alive if person.nationality == "Swedish")
    male = (person for person in swed if person.sex == "male")
    most_young = max(male, key=lambda p: p.birth).name
    print(most_young)

def parse_ranges(ranges):
    for r in ranges.split(","):
        start, end = map(int, r.split("-"))
        yield from range(start, end+1)


def filter_names(names, ignore_char, max_names):
    ic = (person for person in names if person[0].lower() != ignore_char.lower())
    ic_d = (person for person in ic if all(c.isalpha() for c in person))
    return (person for index, person in enumerate(ic_d) if index < max_names)


def second():
    with open("data.csv", "r", encoding="utf-8") as file:
        file_lines = csv.reader(file)
        print(sum((int(line[1]) for line in file_lines if line[2] == "a")))


def years_days(year):
    return (date(year=year, month=month, day=day)
            for month in range(1, 13)
            for day in range(1, calendar.monthrange(year=year, month=month)[1]+1))

def nonempty_lines(file):
    with open(file, "r", encoding="utf-8") as f:
        file_lines = (line.strip("\n") for line in f if len(line.strip("\n")))
        total = (line if len(line)<26 else "..." for line in file_lines)
        yield from total

def txt_to_dict():
    with open("planets.txt", "r", encoding="utf-8") as file:
        file_lines = (line.strip("\n").split(" = ") for line in file if len(line.strip().split(" = "))==2)
        for item in file_lines:
            if item[0] == "Name":
                new_dict = {}
                new_dict.setdefault(item[0], item[1])
            else:
                new_dict.setdefault(item[0], item[1])
            if len(new_dict) == 4:
                yield new_dict


# module_3_2 Генераторные выражения

from collections import Counter
def unique(iterable):
    """iterable без дубликатов"""
    # yield from Counter(iterable)
    # return (item for item in Counter(iterable))
    # yield from dict.fromkeys(iterable)
    return iter(dict.fromkeys(iterable))

def stop_on(iterable, obj):
    """генератор, порождающий последовательность
     элементов итерируемого объекта iterable до тех пор, пока не будет достигнут obj"""
    it = iter(iterable)
    yield from iter(lambda: next(it), obj)
    # return iter(lambda: next(it), obj)

def with_previous(iterable):
    """(<очередной элемент>, <предыдущий элемент>)"""
    new = dict(enumerate(iterable))
    help_dict = {-1:None} | new
    yield from ((v,help_dict[k-1]) for k, v in new.items())

def pairwise(iterable):
    """(<очередной элемент>, <следующий элемент>)"""
    new = dict(enumerate(iterable))
    try:
        help_dict = new | {max(new.keys())+1: None}
        yield from ((v, help_dict[k+1]) for k, v in new.items())
    except:
        pass

def around(iterable):
    """(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)"""
    new = dict(enumerate(iterable))
    try:
        help_dict =  {-1:None} | new | {max(new.keys()) + 1: None}
        yield from ((help_dict[k-1], v, help_dict[k + 1]) for k, v in new.items())
    except:
        pass
