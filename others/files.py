from functools import reduce
from operator import *
import random

# def pretty_print(data, side='-', delimiter='|'):
#     new_data_o = f' {delimiter} '.join([*map(lambda x: str(x), data)])
#     new_data = (f"""{delimiter} {new_data_o} {delimiter}""").split()
#     leng = len(new_data) - 1 + sum([len(i) for i in new_data])
#     loh = [side for _ in range(leng - 2)]
#     print(f" {''.join(loh)} ")
#     print(*new_data)
#     print(f" {''.join(loh)} ")
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# def concat(*args, sep=' '):
#     return f'{sep}'.join([str(i) for i in args])
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# def product_of_odds(data):
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)


# words = 'the world is mine take a look what you have started'.split()
# print(*map(lambda x: f'""{x}""', words))


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: not str(x) == str(x)[::-1], numbers))


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
#            (11, -23),
#            (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
# print(sorted_numbers)


# def compose(func1, func2):
#     return lambda x: func1(func2(x))
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# def arithmetic_operation(operation):
#     dt = {"+": add, "-": sub, "*": mul, "/": truediv}
#     return lambda x, y: dt[operation](x, y)
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))


# print(*sorted(input().split(), key=lambda x: x.lower()))

# print(
#     *sorted(sorted([input() for _ in range(int(input()))]), key=lambda x: sum([ord(i.upper()) - ord('A') for i in x])),
#     sep='\n')


# ml = sorted(sorted([input().split('.') for _ in range(int(input()))]),
#             key=lambda x: sum([int(x[i]) * 256 ** (3 - i) for i in range(len(x))])),
# for i in ml:
#     for j in i:
#         print('.'.join(j))


# file = open('nums.txt')
# print(list(map(int, file.read().split())))
# file.close()


# file = open('prices.txt', encoding='utf-8')
# print(sum(map(lambda x: mul(int(x[1]), int(x[2])), [line.split() for line in file.readlines()])))
# file.close()


# with open('data.txt', encoding='utf-8') as file:
#     print(*[line.rstrip() for line in file.readlines()][::-1], sep='\n')
#     print(*file.readlines()[::-1], sep='')


# with open('numbers.txt', encoding='utf-8') as file:
#     print(*[sum([int(x) for x in line.split()]) for line in file.readlines()], sep='\n')


# with open('nums.txt', encoding='utf-8') as file:
#     m = list(map(lambda line: line.strip(), file.readlines()))
#     total = []
#     for item in m:
#         s = ''
#         for j in item:
#             if j.isdigit():
#                 s += j
#             else:
#                 total.append(s)
#                 s = ''
#         total.append(s)
#     total = list(map(lambda x: int(x) if x != '' else 0, total))
#     print(sum(total))


# with open('file.txt', encoding='utf-8') as file:
#     m = [[word.strip('1234567890.,!?"') for word in line.split()] for line in file.readlines()]
#     count_lines = len(m)
#     count_words = sum(map(lambda x: len(x), m))
#     count_letters = sum(map(lambda x: sum(map(lambda z: len(z), x)), m))
#     print(f'Input file contains:\n{count_letters} letters\n{count_words} words\n{count_lines} lines')
#     print(m)


# with open('first_names.txt', encoding='utf-8') as first_names, open('last_names.txt', encoding='utf-8') as last_names:
#     names = list(zip(map(lambda line: line.strip(), first_names), map(lambda line: line.strip(), last_names)))
#     print(*map(lambda line: ' '.join(line), random.sample(names, 3)), sep='\n')


# with open('population.txt', encoding='utf-8') as file:
#     countries = list(filter(lambda line: line[0] if line[0][0] == 'G' and int(line[-1]) > 500_000 else '',
#                             list(line.strip().split() for line in file.readlines())))
#     [print(line[0]) for line in countries]


# def read_csv():
#     with open('data.csv_unit', encoding='utf-8') as file:
#         keys = file.readline().strip().split(',')
#         values = [line.strip().split(',') for line in file.readlines()]
#         total = [dict(zip(keys, v)) for v in values]
#         return total
# print(read_csv())


# with open('random.txt', 'w', encoding='utf-8') as file:
#     file.writelines([str(random.randint(111, 777)) + '\n' for _ in range(25)])


# with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
#     m = [line.strip() for line in input_file.readlines()]
#     for i, j in enumerate(m, start=1):
#         output_file.write(f'{i}) {j}\n')


# with open('class_scores.txt', encoding='utf-8') as input_file, open('new_scores.txt', 'w',
#                                                                     encoding='utf-8') as output_file:
#     m = [line.split() for line in input_file.readlines()]
#     for i in range(len(m)):
#         num = int(m[i][1])
#         if num in range(95, 101):
#             num = 100
#         else:
#             num += 5
#         output_file.write(f'{m[i][0]} {num}\n')


# with open('goats.txt', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
#     all = [line.strip() for line in goats.readlines()]
#     goats = all[all.index('GOATS') + 1:]
#     colours = [all[i] for i in range(1, all.index('GOATS'))]
#     total = [[color, len(list(filter(lambda line: line == color, goats)))] for color in colours]
#     total_num = int(sum(item[1] for item in total)) * 7 / 100
#     total_total = list(filter(lambda line: int(line[1]) > total_num, total))
#     print(*sorted([item[0] for item in total_total]), sep='\n')

# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     for _ in range(int(input())):
#         with open(input()) as input_file:
#             output_file.write(input_file.read())


# with open('logfile.txt', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
#     data = [line.strip().split(',') for line in input_file.readlines()]
#     for line in data:
#         line[1], line[2] = str(line[1]).lstrip(), str(line[2]).lstrip()
#         line[1], line[2] = int(str(line[1][0:2]) + str(line[1][3:5])), int(str(line[2][0:2]) + str(line[2][3:5]))
#     n_data = list(filter(lambda line: line[2] - line[1] >= 100, data))
#     [print(n_data[i][0]) for i in range(len(n_data))]

# количсетво строк в файле
# with open(input()) as file:
#     x = file.readlines()
#     print(x)


# with open('ledger.txt') as file:
#     cost = sum(map(lambda x: int(x.strip()[1:]), file.readlines()))
#     print(f'${cost}')


# with open('grades.txt') as file:
#     ml = [line.strip().split() for line in file.readlines()]
#     for line in ml:
#         line[1], line[2], line[3] = int(line[1]), int(line[2]), int(line[3])
#     new_ml = filter(lambda line: line[1]>=65 and line[2]>=65 and line[3]>=65, ml)
#     print(len(new_ml))

# with open('words.txt') as file:
#     ml = file.read().split()
#     [print(word) for word in ml if len(word) == max(map(lambda x: len(x), ml))]


# with open(input()) as file:
#     ml = [line.strip() for line in file.readlines()][-10:]
#     [print(word) for word in ml]


# with open(input()) as file_output, open('forbidden_words.txt') as f_words:  #beegeek.txt
#     s = file_output.read()
#     s_lower = s.lower()
#     words = f_words.read().split()
#     for word in words:
#         s_lower = s_lower.replace(word.lower(), '*' * len(word))
#     for i in range(len(s_lower)):
#         if s_lower[i] == '*':
#             print(s_lower[i], end='')
#         else:
#             print(s[i], end='')


# with open('cyrillic.txt', encoding='utf-8') as cyrillica, open('transliteration.txt', 'w', encoding='utf-8') as out_file:
#     d = {
#         'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#         'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#         'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#         'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
#     }
#     s = cyrillica.read()
#     z = list('йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')
#     for i in range(len(s)):
#         if s[i].islower() and s[i].lower() in d:
#             symbol = d[s[i]]
#
#         elif s[i].isupper() and s[i].lower() in d:
#             symbol = d[s[i].lower()].title()
#         else:
#             symbol = s[i]
#         out_file.write(symbol)


with open('answer.txt', encoding='utf-8') as in_file:
    ml = [line.strip() for line in in_file.readlines()]
    new_ml = list(filter(lambda line: 'def' in line, ml))
    preline = ''
    total_ml = []
    for line in ml:
        if line.startswith('def ') and not preline.startswith('#'):
            total_ml.append(f'{line[4:line.find("(")]}')
        preline = line
    print('\n'.join(total_ml) if total_ml else 'Best Programming Team')







