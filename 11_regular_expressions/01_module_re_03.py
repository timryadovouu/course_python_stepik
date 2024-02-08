import re
import sys

"""===================================================SUMMARY======================================================="""
def sub():
    """
    Возвращает строку, полученную путем замены всех найденных неперекрывающихся вхождений регулярного выражения
    pattern в строке string на строку замены repl
    Если шаблон регулярного выражения не найден, строка возвращается без изменений.
    pattern — шаблон регулярного выражения
    repl — строка замены (строка или функция)
    string — строка для поиска
    count=0 — максимальное число замен (необязательный аргумент)
    flags=0 — один или несколько флагов (необязательный аргумент)
    """
    # замена строкой
    text = 'Java самый популярный язык программирования в 2022 году.'
    res = re.sub(r'Java', r'Python', text)
    print(res)

    print()
    text = 'foo.123.bar.456.baz.789.geek'
    result1 = re.sub(r'\d+', r'#', text)
    result2 = re.sub(r'[a-z]+', r'(*)', text)
    print(result1)
    print(result2)

    print()
    result = re.sub(r'(\w+),bar,baz,(\w+)', r'\2,bar,baz,\1', r'foo,bar,baz,qux')
    print(result)
    result = re.sub(r'foo,(\w+),(\w+),qux', r'foo,\g<2>,\g<1>,qux', 'foo,bar,baz,qux')
    print(result)
    result = re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', r'foo,\g<w2>,\g<w1>,qux', r'foo,bar,baz,qux')
    print(result)
    # замена функцией
    def func(match_obj):
        s = match_obj.group(0)  # строка совпадения
        if s.isdigit():
            return str(int(s) * 10)
        else:
            return s.upper()
    result = re.sub(r'\w+', func, r'foo.10.bar.20.baz30.40')
    print(result)
    # count
    print()
    text = ('Java самый популярный язык программирования в 2022 году.'
            ' Язык java — строго типизированный объектно-ориентированный язык программирования общего назначения,'
            ' разработанный компанией Sun Microsystems. Приложения Java обычно транслируются в специальный байт-код,'
            ' поэтому они могут работать на любой компьютерной архитектуре,'
            ' для которой существует реализация виртуальной Java-машины.')
    res = re.sub(r'Java', r'Python', text, count=3, flags=re.I)
    print(res)
def subn():
    """
    Идентична функции sub(), за тем исключением, что она возвращает кортеж,
    состоящий из измененной строки и количества сделанных замен.
    pattern — шаблон регулярного выражения
    repl — строка замены
    string — строка для поиска
    count=0 — максимальное число замен (необязательный аргумент)
    flags=0 — один или несколько флагов (необязательный аргумент)
    """

    text = 'foo.123.bar.456.baz.789.geek'
    result1 = re.subn(r'\d+', r'#', text)
    result2 = re.subn(r'[a-z]+', r'(*)', text, count=2)
    print(result1)
    print(result2)

"""===================================================TASKS========================================================="""
def normalize_jpeg(filename):
    return re.sub(r"jpe?g$", r"jpg", filename, flags=re.I)

def normalize_whitespace(string):
    return re.sub(r"[ ]+", r" ", string)

def task_3(string):
    import keyword
    # def func(match_obj):
    #     s = match_obj.group(0)
    #     if s.lower() in [i.lower() for i in keyword.kwlist]:
    #         return "<kw>"
    #     else:
    #         return s
    # return re.sub(r"\b\w+\b", func, string, flags=re.IGNORECASE)

    words = "|".join(keyword.kwlist)
    return re.sub(fr"{words}", "<kw>", string, flags=re.I)

def task_4(string):
    # def func(match_obj):
    #     s = match_obj.group(0)
    #     if len(s) >= 2:
    #         return f"{s[1]}{s[0]}{s[2:]}"
    #     else:
    #         return s
    # return re.sub(r"\b\w+\b", func, string, flags=re.IGNORECASE)
    return re.sub(r"\b(\w)(\w)", r"\2\1", string)

def task_5(string):
    def func(match_obj):
        return int(match_obj.group(1)) * match_obj.group(2)
    if ")" not in string:
        return string
    return task_5(re.sub(r"(\d+)\((\w+)\)", func, string))
    # print(task_5("bbbb10(2(a))bbb"))
    # print(task_5("hello3(world)hi"))

def task_6(string):
    print(re.sub(r"\b(\w+)(\W+\1\b)+", r"\1", string))
    # task_6("beegeek,beegeek,beegeek!")
    # task_6("beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik")
    # task_6("hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!")
    # task_6("wow Wow wow WOW")

def task_7():
    # print(re.sub(r'[ ]*"""[`\[\]/a-zA-Z.(),:\' \n]+"""\n|[ ]{2}#[ ].*|^[ ]*##?[ ].*\n', r"", sys.stdin.read(), flags=re.MULTILINE))
    print(re.sub(r'(\s*""".*?""")|(\n? *#.*?$)', "", sys.stdin.read(), flags=re.MULTILINE|re.DOTALL))

task_7()






















