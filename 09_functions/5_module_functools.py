import functools
import sys
#example: reduce
'''===================================================SUMMARY======================================================='''
def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'
to_Timur = functools.partial(send_email, "Тимур", "timyrik20@beegeek.ru")
send_an_invitation = functools.partial(send_email, text = "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....")
"""
def cached(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        result = cache.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper
"""
"""
    maxsize=128 — максимальный размер кэша (тип int)
    typed=False — как кэшировать при разных типах аргументов (тип bool)
Если для параметра maxsize установлено значение None, то кэш может расти без ограничений.
Если для typed задано значение True, то аргументы функций разных типов будут кэшироваться отдельно. Например, f(3) и f(3.0)
будут рассматриваться как отдельные вызовы с разными результатами. Если для typed задано значение False, то вызовы будут
рассматриваться как одинаковые.
"""
def fast_fib():
    @functools.lru_cache()
    def fibonacci(n):
        if n <= 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    print(fibonacci(300))



@functools.lru_cache(typed=False)
def simply_dima_1():
    new_list = [line.strip() for line in sys.stdin]
    return "\n".join(["".join(sorted(list(item))) for item in new_list])


@functools.lru_cache()
def ways(n: int) -> int:
    if n <= 3:
        return 1
    elif n == 4:
        return 2
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)

print(ways(6))
