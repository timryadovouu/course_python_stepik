import functools, time
'''===================================================SUMMARY======================================================='''
def first():
    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return '<b>' + func(*args, **kwargs) + '</b>'
        return wrapper

    @bold
    def greet(name):
        '''Функция приветствия пользователя.'''
        return f'Hello {name}!'

    print(greet.__name__)
    print(greet.__doc__)
"""
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper
"""

def decorator_of_time():
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            val = func(*args, **kwargs)
            end = time.perf_counter()
            work_time = end - start
            print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
            return val
        return wrapper
    @timer
    def test(n):
        return sum([(i / 99) ** 2 for i in range(n)])
    @timer
    def sleep(n):
        time.sleep(n)
    res1, res2 = test(10000), sleep(4)
    print(f'Результат функции test = {res1}')
    print(f'Результат функции sleep = {res2}')

def decorator_of_returns_of_func():
    def counter(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.num += 1
            print(f'Вызов {func.__name__}: {wrapper.num}')
            val = func(*args, **kwargs)
            return val
        wrapper.num = 0
        return wrapper
    @counter
    def greet(name):
        return f'Hello {name}!'
    print(greet('Timur'))
    print(greet('Ruslan'))
    print(greet('Arthur'))
    print(greet('Gvido'))
def decorator_to_slow_func():
    def slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(1)
            return func(*args, **kwargs)
        return wrapper
    @slow_down
    def countdown(number):
        if number < 1:
            print('Конец!')
        else:
            print(number)
            countdown(number - 1)
    countdown(5)

def second():
    # делаем универсальный декоратор
    def print_symbols(symbol, length):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(symbol * length)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    @print_symbols('*', 30)
    def add(a, b):
        return a + b
'''===================================================TASKS======================================================='''

def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return wrapper

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args,**kwargs)
            q = 1 / isinstance(result, str)
            return result
        except:
            raise TypeError
    return wrapper

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        info_1 =f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}"
        info_2 = f"TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}"
        print(info_1 + "\n" + info_2)
        return func(*args, **kwargs)
    return wrapper

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return f"{func(*args, **kwargs)}{string}"
            else:
                return f"{string}{func(*args, **kwargs)}"
        return wrapper
    return decorator


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def strip_range(start, end, char="."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = list(func(*args, **kwargs))
            for i in range(start, end):
                if i in range(len(result)):
                    result[i] = char
            return "".join(result)
        return wrapper
    return decorator


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                check = 1/isinstance(func(*args, **kwargs), datatype)
                return func(*args, **kwargs)
            except:
                raise TypeError
        return wrapper
    return decorator

def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                new_list = all([any(isinstance(item, a) for a in types) for item in list(args) + list(kwargs.values())])
                check = 1 / new_list
                return func(*args, **kwargs)
            except:
                raise TypeError
        return wrapper
    return decorator

def add_attrs(**attr):
    def decorator(func):
        func.__dict__.update(attr)
        return func
    return decorator


def ignore_exception(*types_of_errors):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except types_of_errors as err:
                print(f"Исключение {type(err).__name__} обработано")
        return wrapper
    return decorator

class MaxRetriesException(Exception):
    pass
def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            # else:
            raise MaxRetriesException
        return wrapper
    return decorator

