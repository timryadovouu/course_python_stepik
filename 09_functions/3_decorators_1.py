import sys
'''===================================================SUMMARY======================================================='''
def one():
    def null_decorator(func):
        return func
    def say():
        print('Привет Мир!')
    say = null_decorator(say)      # декорируем функцию
    say()
def one_but_better():
    def null_decorator(func):
        return func
    @null_decorator  # декорируем функцию
    def say():
        print('Привет Мир!')
    say()

def two():
    def sample_decorator(func):          # определяем декоратор
        def wrapper():
            print('Начало функции')
            func()
            print('Конец функции')
        return wrapper
    def say():
        print('Привет Мир!')
    say = sample_decorator(say)          # декорируем функцию
    say()

def two_but_better():
    def sample_decorator(func):          # определяем декоратор
        def wrapper():
            print('Начало функции')
            func()
            print('Конец функции')
        return wrapper
    @sample_decorator
    def say():
        print('Привет Мир!')
    say()

def three():
    def uppercase_decorator(func):
        def wrapper():
            original_result = func()
            modified_result = original_result.upper()
            return modified_result
        return wrapper
    @uppercase_decorator
    def greet():
        return 'Hello world!'
    print(greet())

def chetyre():
    def bold(func):
        def wrapper(*args, **kwargs):
            return '<b>' + func(*args, **kwargs) + '</b>'
        return wrapper
    def italic(func):
        def wrapper(*args, **kwargs):
            return '<i>' + func(*args, **kwargs) + '</i>'
        return wrapper

    #greet = bold(italic(greet))
    @bold     #снизу вверх      снизу вверх     снизу вверх
    @italic     #снизу вверх    снизу вверх     снизу вверх
    def greet():
        return 'Hello world!'
    print(greet())

    #Решение заключается в использовании *args и **kwargs во внутренней функции
    @bold
    def greet1(name):
        return f'Hello {name}!'
    @bold
    def greet2():
        return 'Hello world!'
    @bold
    def greet3(name, surname):
        return f'Hello {name} {surname}!'

    print(greet1('Timur'))
    print(greet2())
    print(greet3('Timur', 'Guev'))


def sandwich(func):
    def foo(*args):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args)
        print("---- Нижний ломтик хлеба ----")
        return result
    return foo


# переписать print
def new_decorator(func):
    def wrapper(*args, sep=" ", end=""):
        func(*[str(item).upper() for item in args], sep=sep.upper(), end=end.upper())
    return wrapper

# o_print = print
# @new_decorator
# def print(*args, **kwargs):
#     return o_print(*args, **kwargs)
# or
# print = new_decorator(print)
#
# print("2_magic_methods", "asd", "zxc", sep="-iii-", end="!!!aaa!!!")


def do_twice(func):
    def wrapper(*args, **kwargs,):
        for _ in range(2):
            result = func(*args, **kwargs)
        return result
    return wrapper


def reverse_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result
    return wrapper

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result, 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper



def takes_positive(func):
    def wrapper(*args, **kwargs):
        try:
            check_list = [isinstance(item, int) for item in list(args) + list(kwargs.values())]
            check = 1 / all(check_list)
        except:
            raise TypeError
        try:
            check_list = [item > 0 and isinstance(item, int) for item in list(args) + list(kwargs.values())]
            check = 1 / all(check_list)
        except:
            raise ValueError
        return sum(list(args)+list(kwargs.values()))
    return wrapper
