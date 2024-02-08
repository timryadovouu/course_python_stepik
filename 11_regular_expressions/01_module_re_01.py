import sys
import re
"""===================================================SUMMARY======================================================="""
def search():
    """
    Сканирует строку в поисках первого совпадения с регулярным выражением
    search(pattern, string, flags)
    pattern — шаблон регулярного выражения
    string — строка для поиска
    flags=0 — один или несколько флагов (необязательный аргумент)
    """

    match1 = re.search("super", 'superstition')
    match2 = re.search("super", 'insuperable')
    match3 = re.search("super", 'without')
    print(match1)
    print(match2)
    print(match3)

    print()
    # method group
    match_1 = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
    print(match_1.group())  # вся строка
    print(match_1.group(0))  # вся строка
    print(match_1.group(1))  # подгруппа
    print(match_1.group(2))  # подгруппа
    print(match_1.group(3))  # подгруппа
    print(match_1.group(1, 2, 3))  # кортеж

    print()
    # method group возвращает одну или несколько подгрупп совпадения
    match_2 = re.search(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
    print(match_2.group())
    print(match_2.group('w1'))
    print(match_2.group('w2'))
    print(match_2.group('w3'))
    print(match_2.group('w1', 'w2', 'w3', 'w2', 'w3'))

    print()
    # method groups --- возвращает кортеж, содержащий все захваченные группы.
    match_3 = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
    print(match_3.groups())
    match_3_1 = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
    print(match_3_1.groups(-1))  # позиционный аргумент
    print(match_3_1.groups(''))
    print(match_3_1.groups(default='----'))  # именованный аргумент
    print(match_3_1.groups(default=False))

    print()
    # method groupdict --- возвращает словарь, содержащий все захваченные именованные группы
    # Если именованных групп в исходном регулярном выражении нет, метод groupdict() возвращает пустой словарь.
    match4 = re.search(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
    print(match4.groupdict())
    match_4_1 = re.search(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)?', 'foo,bar,')
    print(match_4_1.groupdict())            # None
    print(match_4_1.groupdict(default=''))
    print(match_4_1.groupdict(default='----'))
search()
def match():
    """
    Возвращает специальный объект соответствия (тип Match), если начало строки соответствуют регулярному выражению
    match(pattern, string, flags)
    pattern — шаблон регулярного выражения
    string — строка для поиска
    flags=0 — один или несколько флагов (необязательный аргумент)
    """
    match1 = re.match('super', 'superstition')
    match2 = re.match('super', 'insuperable')
    print(match1)
    print(match2)

def fullmatch():
    # Возвращает специальный объект соответствия (тип Match), если вся строка соответствует
    # pattern — шаблон регулярного выражения
    # string — строка для поиска
    # flags=0 — один или несколько флагов (необязательный аргумент)
    # fullmatch = search('^\d+$', '123')
    match1 = re.fullmatch(r'\d+', '123foo')
    match2 = re.fullmatch(r'\d+', 'foo123')
    match3 = re.fullmatch(r'\d+', 'foo123bar')
    match4 = re.fullmatch(r'\d+', '123')

    print(match1)
    print(match2)
    print(match3)
    print(match4)
fullmatch()

def escape():
    """
    Функция escape() выполняет экранирование специальных символов в строке
    pattern - шаблон
    """
    print(re.escape('http://www.stepik.org'))

def flags():
    """
    re.IGNORECASE (I) - игнорирует регистр символов
    re.MULTILINE (M) -используется совместно с метасимволами ^ и $,
     в первом случае возвращает совпадения в начале каждой новой строки \n,
      во втором – в конце \n
    re.DOTALL (S) - заставляет метасимвол . возвращать совпадения по абсолютно всем символам, включая \n
    re.VERBOSE (X) - разрешает комментарии в регулярном выражении
    re.DEBUG (-) - показывает отладочную информацию о скомпилированном регулярном выражении
    re.ASCII (A) - указывает кодировку ASCII для классификации символов \w, \W, \b, \B, \d, \D, \s, \S
    re.UNICODE (U) - ...
    re.LOCALE (L) - учитывает региональные настройки при использовании метасимволов \w, \W, \b, \B, \s, \S
    """



"""===================================================TASKS======================================================="""
def task_0(string):
    numbers = filter(lambda item: any([i.isdigit() for i in item]), [item for item in string.split()])
    clear_numbers = []
    for p_num in numbers:
        start = [1 if c.isdigit() else 0 for c in p_num].index(1)
        stop = len(p_num) - [1 if c.isdigit() else 0 for c in p_num[::-1]].index(1)
        clear_num = p_num[start:stop]
        if clear_num.find("-") != -1:
            w = clear_num.split("-")
            if w[0] == "7" and [len(_) for _ in w] == [1, 3, 3, 2, 2]:
                clear_numbers.append(clear_num)
            if w[0] == "8" and [len(_) for _ in w] == [1, 3, 4, 4]:
                clear_numbers.append(clear_num)
            else:
                continue
    print(*clear_numbers, sep="\n")

# task_1("Перезвони мне, пожалуйста: 7-919-667-21-19")
# task_1("Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911")
# task_1("Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221")

def task_1():
    data = [line.strip("\n") for line in sys.stdin]
    format_data = [re.fullmatch(r"(?P<n1>\d{1,3})([- ])?(?P<n2>\d{1,3})\2(?P<n3>\d{4,10})", line) for line in data]
    total_data = [f"Код страны: {line.group('n1')}, Код города: {line.group('n2')}, Номер: {line.group('n3')}" for line in format_data]
    return "\n".join(total_data)

def task_2():
    data = [line.strip("\n") for line in sys.stdin]
    format_data = [re.fullmatch(r"^_[0-9]+[a-zA-Z]*(_?)$", line) for line in data]
    total_data = ["True" if line else "False" for line in format_data]
    return "\n".join(total_data)

def task_3():
    # data = map(str.rstrip, sys.stdin)
    format_data = [re.fullmatch(r"(\w+)\1", line) for line in map(str.rstrip, sys.stdin)]
    return "\n".join([line.group() for line in format_data if line])

def task_4():
    data = list(map(str.rstrip, sys.stdin))
    count_bee = sum([1 for line in data if re.fullmatch(r".*(bee).*\1.*", line)])
    count_geek = sum([1 for line in data if re.fullmatch(r".*(\bgeek\b).*\1?.*", line)])
    return "\n".join(map(str, [count_bee, count_geek]))

def task_5():
    score = 0
    for line in map(str.rstrip, sys.stdin):
        if re.fullmatch(r"^(beegeek).*\1$", line):
            score += 3
        elif re.fullmatch(r"^(beegeek).*|.*(beegeek)$", line):
            score += 2
        elif re.fullmatch(r".+(beegeek).+", line):
            score += 1
    return score

def qwe():
    match_7 = re.search('''\d+  # целая часть
                         \.    # десятичная точка
                         \d*  # дробная часть''', 'Десятичное число равно 123.7', re.VERBOSE)
    print(match_7)

def task_6(string):
    asd = re.search("^((Добрый день)|(Здравствуйте)|(Доброе утро)|(Добрый вечер))", string, flags=re.IGNORECASE)
    if asd: return True
    return False

def task_7():
    return sum([1 for line in map(str.rstrip, sys.stdin) if re.search("beegeek", line, flags=re.I)])




