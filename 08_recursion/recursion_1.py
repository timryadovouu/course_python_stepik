import copy
import sys
'''======================================================SUMMARY======================================================='''

def draw_rect(w,h):
    def rec(step):
        if step < h:
            print("*"*w)
            rec(step+1)
    rec(0)

def print_numbers(start, end):
    def rec(num):
        if num <= end:
            print(num)
            rec(num+1)
    rec(start)

def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n-1)

def from_one_to_h(start):
    if start <101:
        print(start)
        from_one_to_h(start+1)

def qwe(x):
    if x != 0:
        qwe(int(input()))
    print(x)

def triangle(n):
    if n > 0:
        triangle(n-1)
        print("*" * n)

def sand_clock(start):
    if start > 0:
        print(f"{' '*((16-4*start)//2)}{str(5-start)*4*start}")
        sand_clock(start-1)
        print(f"{' '*((16-4*start)//2)}{str(5-start)*4*start}")

def sand_clock_2(start):
    if abs(start) < 4:
        print(f"{' '*((16-4*((abs(start))+1))//2)}{str(4-abs(start))*4*(abs(start)+1)}")
        sand_clock_2(start-1)

def print_digits(number):
    if number / 10 > 0:
        print_digits(number//10)
        print(number % 10)

'''======================================================TASKS======================================================='''

def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)
# print(factorial(5))
# fact = lambda n: 1 if n == 1 else n*fact(n-1)
# print(*map(fact, range(1,11)))
def sum_to(n):
    if n == 0: return 0
    return n + sum_to(n-1)
# print(sum_to(100))

def recursive(my_list):
    if not my_list: return 0
    return my_list[0] + recursive(my_list[1:])
# print(recursive([i+1 for i in range(100)]))

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


cache = {1: 1, 2: 1}
def fib_1(n):
    cache = {1:1, 2:1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
            print(cache)
        return result
    return fib_rec(n)
# print(fib_1(5))

def how_many_chars_int(number):            #Количество цифр
    if not str(number): return 0
    return 1 + len(str(number)[1:])
# print(how_many_chars_int(int(input())))
h = lambda n: 0 if not str(n) else 1+len(str(n)[1:])
# print(h(int(input())))

h_1 = lambda n: 0 if not n else n%10 + h_1(n//10)         #Сумма цифр
# print(h_1(int(input())))

def number_of_frogs(year):
    if year == 1: return 77
    return 3*(number_of_frogs(year-1)-30)
number_of_frogs_1 = lambda year: 77 if year == 1 else 3*(-30+h_2(year-1))

def range_sum(numbers, start, end):
    if start == end: return numbers[start]
    return numbers[start] + range_sum(numbers, start+1, end)
range_sum_1 = lambda numbers, start, end: numbers[start] if start == end else numbers[start] + range_sum_1(numbers, start+1, end)

def get_pow(a, n):
    if n == 0: return 1
    return a* get_pow(a, n-1)

def get_fast_pow(a, n):
    if n == 0: return 1
    elif n%2 == 0:
        return get_fast_pow(a**2, n//2)
    else:
        return a * get_fast_pow(a, n-1)

def recursive_sum(a, b):
    if a == 0 or b==0: return b+a
    else:
        return 1 + recursive_sum(a-1, b)

def is_power(number):
    if number <=2: return True
    elif number%2:
        return False
    return is_power(number//2)

def tribonacci(n):
    cache = {1: 1, 2: 1, 3:1}
    def tribonacci_rec(n):
        result = cache.get(n)
        if result is None:
            cache.setdefault(n, tribonacci_rec(n - 2) + tribonacci_rec(n - 1) + tribonacci_rec(n-3))
        return cache[n]
    return tribonacci_rec(n)

def is_palindrome(string):
    if len(string) in range(0,2): return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

def to_binary_vol1(number):
    if number == 0: return 0
    else:
        return int(str(to_binary_vol1(number//2)) + str(number%2))
def to_binary_vol2(number):
    if number <= 1:
        return str(number)
    return to_binary_vol2(number // 2) + str(number % 2)

def loop(number):
    print(number)
    if number>0:
        loop(number-5)
        print(number)
# loop(16)

'''======================================================LAST_TASKS======================================================='''

#меняем глубину рекурсии
def change_depth():
    limit = sys.getrecursionlimit()
    print(limit)
    sys.setrecursionlimit(6000)
    new_limit = sys.getrecursionlimit()
    print(new_limit)
    return True

def recursive_sum_1(nested_lists):
    counter = 0
    if not nested_lists:
        return 0
    if type(nested_lists) == int:
       counter += nested_lists
    elif type(nested_lists) == list:
        for k in nested_lists:
            counter += recursive_sum_1(k)
    return counter

# my_list = [1, [4, 4], 2, [1, [2, 10]]]
# print(recursive_sum_1(my_list))
def linear(nested_lists):
    answer = []
    if type(nested_lists) == int:
        answer.append(nested_lists)
    if type(nested_lists) == list:
        for item in nested_lists:
            answer += linear(item)
    return answer


def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_value(v,key)
            if value is not None:
                return value

def get_all_values(nested_dicts, key):
    answer = []
    if key in nested_dicts:
        answer.append(nested_dicts[key])
    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_all_values(v,key)
            if value is not None:
                answer += value
    return answer


def dict_travel(nested_dicts, val=''):
    for k, v in sorted(nested_dicts.items()):
        if type(v) == dict:
            dict_travel(v, val + f"{k}.")
        else:
            print(f"{val}{k}: {v}")
    return None

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)
print()
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
dict_travel(data)
print()
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)