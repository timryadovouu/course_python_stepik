import itertools as it
from collections import namedtuple

"""===================================================SUMMARY======================================================="""
"""
1.порождающие данные 
2.фильтрующие данные 
3.преобразующие данные
4.группирующие данные <-- про это в данном блоке (только groupby)
5.объединяющие или разделяющие данные 
6.порождающие комбинаторные данные
"""

def group_by():
    """
    Используется для группировки смежных элементов итерируемого объекта.
    Возвращает итератор, содержащий кортежи, каждый из которых состоит из двух элементов:
    первый — значение, характеризующее группу,
    второй — итератор, содержащий элементы соответствующей группы.
    groupby(iterable, key)
    iterable — итерируемый объект
    key — функция, вычисляющая значение, характеризующее группу
    Если key не указан или None, ключом по умолчанию является функция тождественности, которая возвращает элемент без изменений.
    """

    numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
    group_iter = it.groupby(numbers)
    # print(type(group_iter))
    # print(*group_iter, sep='\n')
    for key, values in group_iter:
        print(f'{key}: {list(values)}')
    print()

    numbers_1 = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
    group_iter = it.groupby(sorted(numbers_1))
    for key, values in group_iter:
        print(f'{key}: {list(values)}')
    print()

    numbers_2 = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
    group_iter = it.groupby(numbers_2, key=lambda num: num < 10)
    for key, values in group_iter:
        print(f'{key}: {list(values)}')

"""===================================================TASKS======================================================="""

def task_1():
    Person = namedtuple('Person', ['name', 'age', 'height'])
    persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
               Person('Mark', 71, 172), Person('Alex', 45, 193),
               Person('Jeff', 63, 193), Person('Ryan', 41, 184),
               Person('Ariana', 28, 158), Person('Liam', 69, 193)]

    new_arr = it.groupby(sorted(persons, key=lambda person: person.height), key=lambda person: person.height)
    [print(f"{_}: {', '.join([per.name for per in sorted(v, key=lambda p: p.name)])}") for _, v in new_arr]

def task_2():
    Student = namedtuple('Student', ['surname', 'name', 'grade'])
    students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
                Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
                Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
                Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
                Student('Елькина', 'Мария', 11), Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
                Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
                Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
                Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
                Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]

    arr = max(it.groupby(sorted(students, key=lambda p: p.name), key=lambda st: st.name),
              key=lambda tpl: sum(1 for _ in tpl[1]))
    print(arr[0])

def task_3():
    data = input().split()
    arr = it.groupby(sorted(data, key=lambda item:len(item)), key=lambda i: len(i))

    for k, v in arr:
        print(f"{k} -> {', '.join(sorted(v))}")

def task_4():
    tasks = [('Отдых', 'поспать днем', 3),
             ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
             ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
             ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
             ('Отдых', 'погулять вечером', 4),
             ('Курс по ооп', 'обсудить темы', 1),
             ('Урок по groupby', 'добавить задачи на программирование', 3),
             ('Урок по groupby', 'написать конспект', 1),
             ('Отдых', 'погулять днем', 2),
             ('Урок по groupby', 'добавить тестовые задачи', 2),
             ('Уборка', 'убраться в ванной', 2),
             ('Уборка', 'убраться в комнате', 1),
             ('Уборка', 'убраться на кухне', 3),
             ('Отдых', 'погулять утром', 1),
             ('Курс по ооп', 'обсудить задачи', 2)]
    t_tasks = it.groupby(sorted(tasks), key=lambda i: i[0])

    for k, v in t_tasks:
        print(f"{k}:")
        [print(f"    {item[2]}. {item[1]}") for item in sorted(v, key=lambda tpl:tpl[2])]
        print()

def group_anagrams(words):
    new_arr = it.groupby(sorted(words, key=lambda w: sorted(list(w))), key=lambda word: "".join(sorted(list(word))))
    return [tuple(v) for _, v in new_arr]


def ranges(numbers):
    arr = it.groupby(numbers, key=lambda num: num-numbers.index(num))
    answer = []
    for _, v in arr:
        q =list(v)
        answer.append((q[0],q[-1]))
    return answer
# numbers = [1, 2, 3, 4, 7, 8, 10]
# print(ranges(numbers))
#
# numbers = [1, 3, 5, 7]
#
# print(ranges(numbers))
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# print(ranges(numbers))