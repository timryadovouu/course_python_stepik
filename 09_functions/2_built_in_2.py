import sys
'''===================================================SUMMARY======================================================='''
def foo():
    print(callable(int))    # возвращает True, если переданный объект является вызываемым
    print(callable(list))
    print(callable(100))
    print(callable([1, 2, 3]))
    # True
    # True
    # False
    # False

    print(hasattr('stepik', 'isalpha'))
    print(hasattr([1, 2, 3], 'sort'))
    print(hasattr(13, 'to_str'))
    # True
    # True
    # False

    print(hash(899))       # возвращает целое число, представляющее хеш-значение переданного объекта
    print(hash(69.0))      #у -1 ==> -2  <..-4 -3 -2 -2 0 1 2 3 4..>
    print(hash('timyrik'))
    print(hash((1, 2, 3)))
    print(hash(False))
    print(hash(True))
    # 899
    # 69
    # 1468304915
    # -378539185
    # 0
    # 1

    # help(print)
    # help('sorted')

    print(repr('stepik'))          #возвращает строку
    print(repr([1, 2, 3, 4]))

    #Функция eval() выполняет строку-выражение, переданную ей в качестве обязательного аргумента, и возвращает результат выполнения этой строки
    expression = '7 + 10'
    result = eval(expression)
    print(type(result))
    print(result)
    # <class 'int'>
    # 17
    expression1 = "print('Привет из функции eval()')"
    expression2 = "len([1, 1, 1, 1, 1])"
    result1 = eval(expression1)
    result2 = eval(expression2)
    print(result1)
    print(result2)
    # Привет из функции eval()
    # None
    # 5
    list_data = eval("['Python', 'C#', 'Java']")
    tuple_data = eval('(1, 2, 3, 4, 5)')
    dict_data = eval("{1: 'January', 2: 'February'}")
    print(type(list_data), len(list_data))
    print(type(tuple_data), max(tuple_data))
    print(type(dict_data), dict_data[2])
    # <class 'list'> 3
    # <class 'tuple'> 5
    # <class 'dict'> February

    #Функция exec(), в отличие от eval(), принимает блок кода и выполняет его, возвращая значение None
    code = '''a = 10 
    b = 20
    print(a + b)'''
    exec(code)  #30
    code1 = 'print(sorted([3, 5, 4, 1, 2]))'
    code2 = 'print(sum([3, 5, 4, 1, 2]))'
    code3 = 'print(len([3, 5, 4, 1, 2]))'
    exec(code1)     # [1, 2, 3, 4, 5]
    exec(code2)     # 15
    exec(code3)     # 5
    numbers = [1, 2, 3, 4, 5]
    info = {'name': 'Timur', 'surname': 'Guev'}
    code1 = '''total = 0
    for i in numbers:
        total += i
    print(total)'''
    code2 = 'print(info["name"], info["surname"])'
    exec(code1)     #15
    exec(code2)     #Timur Guev

'''===================================================TASKS======================================================='''
"""def make_adder(n):
    def add(x):
        return x + n
    return add
    
def multiplier_of(n):
    def mult(x):
        return x * n
    return mult

Приведенный ниже код:
plus_3 = make_adder(3)
plus_5 = make_adder(5)
multiply_3 = multiplier_of(3)
multiply_5 = multiplier_of(5)

print(plus_3(10), plus_3(100))
print(plus_5(10), plus_5(100))
print(multiply_3(10), multiply_3(100))
print(multiply_5(10), multiply_5(100))

выводит:
13 103
15 105
30 300
50 500

можно переписать в виде:
def make_adder(n):
    return lambda x: x + n

def multiplier_of(n):
    return lambda x: x * n"""

"""def line_generator(k, b):
    def func(x):
        return k * x + b
    return func

Приведенный ниже код:
line_func_1 = line_generator(2, 5)        # получаем функцию y = 2*x + 5
line_func_2 = line_generator(-6, 9)       # получаем функцию y = -6*x + 9

print(line_func_1(10))                    # печатаем значение 2*10 + 5
print(line_func_2(4))                     # печатаем значение -6*4 + 9"""

def hash_as_key(objects):
    o_dict = {}
    [o_dict.setdefault(hash(item), []).append(item) for item in objects]
    return {k: v[0] if len(v)==1 else v for k,v in o_dict.items()}

def max_from_stdin():
    data = max([eval(line.strip()) for line in sys.stdin])
    return data
def max_min_func():
    function = input()
    a, b = map(int, input().split())
    data = [eval(function) for x in range(a, b+1)]
    answer = [f"Минимальное значение функции {function} на отрезке [{a}; {b}] равно {min(data)}",
              f"Максимальное значение функции {function} на отрезке [{a}; {b}] равно {max(data)}"]
    return "\n".join(answer)


# print_operation_table = lambda args, rows, cols: [print(*[str(args(j+1, i+1)).ljust(4) for i in range(cols)]) for j in range(rows)]

def verification(login, password, success, failure):
    check_letter = list(filter(lambda item: item.isalpha() and ord(item.lower()) in range(ord('a'), ord('z')+1), list(password)))
    check_low_letter = list(filter(lambda item: item.islower() and ord(item.lower()) in range(ord('a'), ord('z')+1), list(password)))
    check_up_letter = list(filter(lambda item: item.isupper() and ord(item.lower()) in range(ord('a'), ord('z')+1), list(password)))
    check_number = list(filter(lambda item: item.isdigit(), list(password)))
    new_list = [check_letter, check_up_letter, check_low_letter, check_number]

    if all(new_list):
        success(login)
    else:
        errors = ["в пароле нет ни одной буквы",
                  "в пароле нет ни одной заглавной буквы",
                  "в пароле нет ни одной строчной буквы",
                  "в пароле нет ни одной цифры"]
        text = errors[new_list.index([])]
        failure(login, text)


def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    data = sum(filter(lambda item: type(item) == int or type(item) == float, elems))
    if data: return data
    else: return 0


#переопределение обычного print'а
# new_print = print
# def print(*args, sep=" ", end=""):
#     return new_print(*[line.upper() if isinstance(line, str) else line for line in args], sep=sep.upper(), end=end.upper())


def polynom(x):
    polynom.__dict__.setdefault("values", set())
    polynom.values.add(x**2+1)
    return x**2+1
# polynom(1)
# polynom(2)
# polynom(3)
# print(*sorted(polynom.values))


def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    for char in text:
        if char in marks:
            text = text.replace(char, "")
    remove_marks.count += 1
    return text



def power(degree):
    def total(num):
        return num**degree
    return total

# def power(degree):
#     return lambda num: num**degree

def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c

def sourcetemplate(url):
    def foo(**kwargs):
        if not kwargs:
            return url
        else:
            add_str = "&".join(sorted([f"{key}={kwargs[key]}" for key in kwargs]))
            return url + "?" + add_str
    return foo
# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load(name='timur'))
# url = 'https://stepik.org/lesson/651459/step/14'
# load = sourcetemplate(url)
# print(load(thread='solutions', unit=648165))


from datetime import date
def date_formatter(country_code):
    def ru(dt):
        return date.strftime(dt, "%d.%m.%Y")
    def us(dt):
        return date.strftime(dt, "%m-%d-%Y")
    def ca(dt):
        return date.strftime(dt, "%Y-%m-%d")
    def br(dt):
        return date.strftime(dt, "%d/%m/%Y")
    def fr(dt):
        return date.strftime(dt, "%d.%m.%Y")
    def pt(dt):
        return date.strftime(dt, "%d-%m-%Y")
    return eval(country_code)
# date_ru = date_formatter('us')
# today = date(2022, 1, 25)
# print(date_ru(today))

def sort_priority(values, group):
    values.sort(key=lambda x: (x not in group, x))
    # numbersMax = max(values)
    # groupMax = max(group)
    # values.sort(key=lambda x: x if x in group else x + groupMax + numbersMax)
# numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# sort_priority(numbers, (300, 100, 200))
# print(numbers)
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {5, 7, 2, 3}
# sort_priority(numbers, group)
# print(numbers)

"""===================================================TYPES========================================================="""

from typing import Union, Optional, Any, NoReturn
def add_or_concatenate(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
    return a + b
# NumberOrStr = Union[int, float, str]
# def add_or_concatenate(a: NumberOrStr, b: NumberOrStr) -> NumberOrStr:
#     return a + b
# print(add_or_concatenate("w","e"))

def opt():
    name: Union[str, None]        #эквивалентно
    name: Optional[str]
    # В Python 3.10 вместо записи Union[X, Y] можно писать X | Y.

def func(arg: Any) -> Any:  #может принимать на вход абсолютно что угодно.
    return arg

def stop() -> NoReturn:    #никогда не возвращает значение
    raise RuntimeError('no way')

def get_digits(number: int|float) -> list[int]:
    return list(map(int, filter(lambda item: item.isdigit(), str(number))))

def top_grade(grades: dict[str, str|list[int]]) -> dict[str, str|int]:
    grades.setdefault("top_grade", max(grades.pop("grades")))
    return grades

def cyclic_shift(numbers: list[int|float], step: int) -> None:
    if step > 0:
        numbers[:] = numbers[len(numbers)-step%len(numbers):len(numbers)] + numbers[0:len(numbers)-step%len(numbers)]
    elif step < 0:
        numbers[:] = numbers[0-step%len(numbers):len(numbers)] + numbers[0:-step%len(numbers)]
    else:
        numbers[:] = numbers

def matrix_to_dict(matrix: list[list[int|float]]) -> dict[int, list[int|float]]:
    new_dict = {}
    [new_dict.setdefault(pair[0], pair[1]) for pair in enumerate(matrix, 1)]
    return new_dict





