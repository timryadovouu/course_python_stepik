from functools import reduce
from operator import *

# abscissas = [*map(float, input().split())]
# ordinates = [*map(float, input().split())]
# applicates = [*map(float, input().split())]
# dots = zip(abscissas, ordinates, applicates)
# result = all(map(lambda item: item[0] ** 2 + item[1] ** 2 + item[2] ** 2 <= 4, zip(abscissas, ordinates, applicates)))
# print(result)

# print(all(map(lambda x: x.isdigit() and int(x) in range(0, 256), input().split('.'))))


# a, b = int(input()), int(input())
# numbers = [i for i in range(a, b + 1)]
#
#
# def isit(x):
#     listik = [int(i) for i in str(x) if i != 0]
#     for i in listik:
#         if x % i != 0 or 0 in listik:
#             return False
#     return True
#
#
# def isit(num):
#     return (all(map(lambda x: int(x) and num % int(x) == 0, str(num))))

# print(*filter(lambda x: isit(x), numbers))
#
# print(*filter(isit, numbers))


# stroka = input()
# print('YES' if all([
#     any(map(lambda x: ord(x) in range(ord('a'), ord('z') + 1), stroka)),
#     any(map(lambda x: ord(x) in range(ord('A'), ord('Z') + 1), stroka)),
#     any(map(lambda x: x.isdigit(), stroka)),
#     len(stroka) >= 7]) else 'NO')


# print('YES' if all([any(map(lambda x: x == 5, [int(input().split()[1]) for _ in range(int(input()))]))
#                     for _ in range(int(input()))]) else 'NO')
result = []
for _ in range(int(input())):
    result.append(any(map(lambda x: x == 5, [int(input().split()[1]) for_ in range(int(input()))])))

print('YES' if all(result) else 'NO')

# result = []
# for _ in range(int(input())):
#     marks = []
#     for _ in range(int(input())):
#         marks.append(int(input().split()[1]))
#     result0 = any(map(lambda x: x == 5, marks))
#     result.append(result0)
#
# print('YES' if all(result) else 'NO')
