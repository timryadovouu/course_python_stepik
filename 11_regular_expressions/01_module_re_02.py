import re
import sys
"""===================================================SUMMARY======================================================="""
def findall():
    """
    Возвращает все неперекрывающиеся совпадения с регулярным выражением в виде списка строк.
    pattern — шаблон регулярного выражения
    string — строка для поиска
    flags=0 — один или несколько флагов (необязательный аргумент)
    """

    text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
    result = re.findall('\d+', text)
    print(result) # ['25', '2', '69']

    print()
    result = re.findall('#(\w+)#', '#foo#.#bar#.#baz#')
    print(result) # ['foo', 'bar', 'baz']

    print()
    result1 = re.findall('(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
    result2 = re.findall('(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
    print(result1) # [('foo', 'bar'), ('baz', 'qux'), ('quux', 'corge')]
    print(result2) # [('foo', 'bar', 'baz'), ('qux', 'quux', 'corge')]

    print()
    result = re.findall('(\w+),(\w+),(\w+)?', 'foo,bar,')
    print(result)   #[('foo', 'bar', '')]
def finditer():
    """
    Возвращает все неперекрывающиеся совпадения с регулярным выражением в виде итератора,
    содержащего объекты соответствия (тип Match).
    pattern — шаблон регулярного выражения
    string — строка для поиска
    flags=0 — один или несколько флагов (необязательный аргумент)
    """

    text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
    result = re.finditer('\d+', text)
    print(type(result))        # <class 'callable_iterator'>
    print(list(result))

    print()
    result = re.finditer('#(\w+)#', '#foo#.#bar#.#baz#')
    for match in result:
        print(match)
        print(match.group(), match.group(1))
        print(match.groups())
"""===================================================TASKS========================================================="""

def task_1():
    article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

    counter_2 = len(re.findall(r"(\.\.\.|!)$", article, flags= re.M))
    counter_1 = len(re.findall("^stepik", article, re.I|re.M))
    print(counter_1)
    print(counter_2)

def task_2(string, word):
    print(len(re.findall(rf"\B{word}\B", string)))


def task_3(string, word):
    print(re.findall(rf"\b{word}\b", string))

def task_4(word, text):
    print(len(re.findall(rf"\b{word[:-2]}[sz]e\b", text, flags=re.IGNORECASE)))

def task_5(word, text):
    print(len(re.findall(rf"\b{word[:-3]}ou?r\b", text, flags=re.IGNORECASE)))

def abbreviate(phrase):
    """должна вернуть аббревиатуру"""
    fnd = re.findall(r"(\b[a-z]|[A-Z])", phrase)
    print("".join(fnd).upper())

def task_html():
    data = map(str.rstrip, sys.stdin)
    #1
    fnd_list = [re.findall(r"<a href=\"(.+)\">(.+)</a>", line) for line in data]
    [print(f"{pair[0][0]}, {pair[0][1]}") for pair in fnd_list]
    #2
    # fnd_list_1 = [[*re.findall(r'href="(.+)">', line), *re.findall(r'<a .+">(.+)</a>', line)] for line in data if "href" in line]
    # print("\n".join([", ".join(pair) for pair in fnd_list_1]))

def html():
    # data = map(str.rstrip, sys.stdin)
    # Dict = {}
    # fnd_list = [re.findall(r"<(\w+)|\b([a-z\-]+)=", line) for line in data if line.strip()[1] != "/"]
    # for lst in fnd_list:
    #     for pair in lst:
    #         if pair[0]:
    #             k = pair[0]
    #             Dict.setdefault(k, [])
    #         else:
    #             if pair[1] not in Dict[k]:
    #                 Dict[k].append(pair[1])
    # print("\n".join([f"{k}: {', '.join(sorted(Dict[k]))}" for k in sorted(Dict)]))
    Dict = {}
    for line in map(str.rstrip, sys.stdin):
        for tag, params in re.findall(r"<(\w+)(.*?)>", line):
            Dict.setdefault(tag, set()).update(re.findall(r"([\w-]+)=", params))
    print(Dict)

















