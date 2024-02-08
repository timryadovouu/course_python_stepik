import random


class Counter:
    def __init__(self, low, high):  # конструктор принимает два аргумента low и high (помимо self)
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

# counter1 = Counter(3, 10)         # создаем итератор Counter, передавая значения low=3, high=10
#
# for i in counter1:                # неявно вызываем функцию next()
#     print(i)
#
# counter2 = Counter(100, 103)      # создаем итератор Counter, передавая значения low=100, high=103
# print(next(counter2))             # явно вызываем функцию next()
# print(next(counter2))             # явно вызываем функцию next()
class EvenNumbers:
    def __init__(self, begin):  # конструктор принимает один аргумент begin (помимо self)
        self.begin = begin + begin % 2
    def __iter__(self):
        return self
    def __next__(self):
        value = self.begin
        self.begin += 2
        return value

# evens1 = EvenNumbers(1)
# for index, num in enumerate(evens1):
#     if index > 5:
#         break
#     print(num)

class StringWrapper:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.index = -1  # вспомогательное поле для отслеживания текущего индекса
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        return self.symbol + self.text[self.index] + self.symbol


# string_wrapper1 = StringWrapper('beegeek', '~')
# for char in string_wrapper1:
#     print(char)
# string_wrapper2 = StringWrapper('Python', '+')
# print(next(string_wrapper2))
# print(next(string_wrapper2))
# print(next(string_wrapper2))
# print(list(StringWrapper('stepik', '-')))

class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value

# infinite_factorials = Factorials()
# for index, num in enumerate(infinite_factorials, 1):
#     if index <= 10:
#         print(f'Факториал числа {index} равен {num}')
#     else:
#         break


class Repeater:
    def __init__(self, obj):
        self.obj = obj
    def __iter__(self):
        return self
    def __next__(self):
        return self.obj

class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= self.times:
            raise StopIteration
        else:
            return self.obj

class Square:
    def __init__(self, n):
        self.n = n
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.start += 1
        if self.start > self.n:
            raise StopIteration
        else:
            return (self.start)**2
class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.first, self.second = self.second, self.first+self.second
        return self.first

class PowerOf:
    def __init__(self, number):
        self.number = number
        self.start = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.start += 1
        return self.number**(self.start)

class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.start = -1
    def __iter__(self):
        return self
    def __next__(self):
        dict_keys = [*self.data]
        self.start += 1
        if self.start >= len(dict_keys):
            raise StopIteration
        else:
            return dict_keys[self.start], self.data[dict_keys[self.start]]

class CardDeck:
    def __init__(self):
        self.card = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.mast = ("пик", "треф", "бубен", "червей")
        self.i_card = -1
        self.i_mast = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i_card += 1
        if self.i_mast > 3:
            raise StopIteration
        elif self.i_card > 12:
            if self.i_mast > 3:
                raise StopIteration
            else:
                self.i_card = -1
                self.i_mast += 1
                return self.__next__()
        else:
            return f"{self.card[self.i_card]} {self.mast[self.i_mast]}"

class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self
    def __next__(self):
        # self.start += 1
        # return self.iterable[self.start%len(self.iterable)]
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

class RandomNumbers:
    def __init__(self, left, right, n):
        self.data = (random.randint(left, right) for _ in range(n))
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.data)

class Alphabet:
    def __init__(self, language):
        self.language = language
        if self.language == "ru":
            self.iterator = iter(range(ord("а"), ord("я")+1))
        else:
            self.iterator = iter(range(ord("a"), ord("z")+1))
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return chr(next(self.iterator))
        except StopIteration:
            if self.language == "ru":
                self.iterator = iter(range(ord("а"), ord("я") + 1))
            else:
                self.iterator = iter(range(ord("a"), ord("z") + 1))
            return chr(next(self.iterator))


class Xrange:
    def __init__(self, start, end, step=1):
        if isinstance(step, int) and isinstance(start, int) and isinstance(end, int):
            self.d = "//"
        else:
            self.d = "/"
        self.iterator = iter(range(int(start*100), int(end*100), int(step*100)))

    def __iter__(self):
        return self
    def __next__(self):
        return eval(f"{next(self.iterator)}{self.d}100")

# xrange = Xrange(5.9, 44, 3)
# print(tuple(xrange))