import re
"""===================================================SUMMARY======================================================="""
def split():
    """
    Разбивает строку на подстроки, используя регулярное выражение в качестве разделителя, и возвращает подстроки в виде списка.
    pattern — шаблон регулярного выражения
    string — строка для поиска
    maxsplit=0 — максимальное количество разбиений (необязательный аргумент)
    flags=0 — один или несколько флагов (необязательный аргумент)
    если maxsplit является отрицательным числом, то re.split() возвращает исходную строку без изменений.
    """

    result = re.split(r'[,;.]', 'foo,bar.baz;qux;stepik,beegeek')
    print(result)  # ['foo', 'bar', 'baz', 'qux', 'stepik', 'beegeek']

    result = re.split(r'\s*[,;.]\s*', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
    print(result)

    result1 = re.split(r'\s*([,;.])\s*', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
    result2 = re.split(r'(\s*[,;.]\s*)', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
    print(result1)
    print(result2)

    result = re.split(r'(?:\s*[,;.]\s*)', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
    print(result)  # ['foo', 'bar', 'baz', 'qux', 'stepik', 'beegeek']

    print()
    text = 'foo; bar;   baz; qux;   stepik;    beegeek'
    regex = r';\s*'
    result1 = re.split(regex, text)
    result2 = re.split(regex, text, maxsplit=2)
    result3 = re.split(regex, text, maxsplit=4)
    print(result1)
    print(result2)
    print(result3)
    def foo():
        string = 'foo,bar.baz;  qux;stepik,    beegeek'
        regex = r'(\s*[,;.]\s*)'
        res = re.split(regex, string)
        for index, value in enumerate(res):
            if not re.fullmatch(regex, value):
                res[index] = f'[{value}]'
        new_string = ''.join(res)
        print(string)
        print(new_string)

def compile():
    """
    Модуль re поддерживает возможность предварительной компиляции регулярного выражения в специальный объект,
    который можно повторно использовать позже. Для этого используется функция compile()
    regex — шаблон регулярного выражения
    flags=0 — один или несколько флагов (необязательный аргумент)
    """
    # regex_obj = re.compile('\d')
    # print(type(regex_obj))
    # <class 're.Pattern'>


    # 1 способ --- шаблон регулярного выражения
    regex_obj = re.compile('\d+')
    text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
    result = re.findall(regex_obj, text)
    print(result)
    # общий случай
    # regex_obj = re.compile(<regex>, <flags>)
    # result = re.search(regex_obj, <string>)     # match(), fullmatch(), findall(), finditer()


    # 2 способ --- можем вызывать функции как методы непосредственно из объекта регулярного выражения
    regex_obj = re.compile('\d+')
    text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
    result = regex_obj.findall(text)
    print(result)
    # общий случай
    # regex_obj = re.compile( < regex >, < flags >)
    # result = regex_obj.search( < string >)  # match(), fullmatch(), findall(), finditer()

    def bar():
        regex_obj = re.compile('ba[rz]', flags=re.I)
        result1 = re.search('ba[rz]', 'FOOBARBAZ', flags=re.I)
        result2 = re.search(regex_obj, 'FOOBARBAZ')
        result3 = regex_obj.search('FOOBARBAZ')
        print(result1)  # <re.Match object; span=(3, 6), match='BAR'>
        print(result2)  # <re.Match object; span=(3, 6), match='BAR'>
        print(result3)  # <re.Match object; span=(3, 6), match='BAR'>

    # Скомпилированный объект регулярного выражения поддерживает следующие методы:
    # search(string, pos, endpos)
    # match(string, pos, endpos)
    # fullmatch(string, pos, endpos)
    # findall(string, pos, endpos)
    # finditer(string, pos, endpos)
    regex_obj = re.compile('\d+')
    text = 'foo12345barbaz'
    print(regex_obj.search(text))
    print(regex_obj.search(text, pos=4))
    print(regex_obj.search(text, endpos=7))
    print(regex_obj.search(text, pos=4, endpos=7))
"""===================================================TASKS========================================================="""
def task_1(string):
    print(*re.split(r"\s*[.,;]\s*", string))

def task_2(string):
    print(*re.split(r"\s(?:and|or|[|&])\s*", string), sep=", ")

def multiple_split(string, delimiters):
    pattern = "|".join(map(re.escape, delimiters))
    return re.split(fr"{pattern}", string)

    # print(multiple_split('beegeek-python.stepik', ['.', '-']))
    # print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
    # print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))

def TheLastTask():
    a, b = map(int, input().split())
    regex_obj = re.compile(r"\d+")
    print(sum(map(int, regex_obj.findall(input(), pos=a, endpos=b))))
    # TheLastTask()