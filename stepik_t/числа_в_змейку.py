from math import *
s = input().split()
#matrix = [[int(i) for i in input().split()] for _ in range(n)]
#matrix_total = [['.']*8 for i in range(8)]
#matrix = [[str(int(i+1)+int(s[1])*k).ljust(3) for i in range(int(s[1]))] for k in range(int(s[0]))]
#n, m = int(s[0]), int(s[1])
matrix = [[str(int('0')).ljust(3) for i in range(int(s[1]))] for _ in range(int(s[0]))]
#m_m = [str(int(i+1)).ljust(3) for i in range(int(s[1]))]
n, m = int(s[0]), int(s[1])
n1, m1 = int(s[0]), int(s[1])
step_count = min(n,m)*2
if n == 1 or m == 1:
    step_count = 2
qwe = 0
if n == m and n % 2 != 0:
    step_count = n*2 - 1
    qwe = 1
nuka = floor(n/2)
counter = 0
char = 1
q = 0
w = n-1
m_vpravo_start = 0
m_vpravo_stop = m - 1
n_vverh_start = 0
n_vverh_stop = n - 1
t = 0
if n == 1 and m == 1:
    matrix[0][0] = str(1).ljust(3)
while counter <= step_count and (n!=1 and m!=1):
    for _ in range(1):            #заполянем вправо
        if qwe == 1 :
            matrix[nuka][nuka] = str(n*m).ljust(3)
        for c in range(m_vpravo_start, m_vpravo_stop):
            matrix[q][c] = str(char).ljust(3)
            char += 1
    counter += 1

    for _ in range(1):             #заполянем вниз
        for r in range (n_vverh_start, n_vverh_stop):
            matrix[r][m_vpravo_stop] = str(char).ljust(3)
            char += 1
    counter += 1


    for _ in range(1):              #заполянем влево
        for c in range(m_vpravo_stop, m_vpravo_start, -1):
            matrix[w][c] = str(char).ljust(3)
            char += 1
    counter += 1

    for _ in range(1):               #заполянем вверх
        for r in range (n_vverh_stop, n_vverh_start, -1):
            matrix[r][m_vpravo_start] = str(char).ljust(3)
            char += 1
    counter += 1

    q += 1
    w -= 1
    m_vpravo_start, m_vpravo_stop = m_vpravo_start + 1, m_vpravo_stop - 1
    n_vverh_start, n_vverh_stop = n_vverh_start + 1, n_vverh_stop - 1
    counter += 1
#print(m_vpravo_start, m_vpravo_stop, nuka, step_count, counter)
if n1 == 1:
    matrix = [[str(int(i+1)).ljust(3) for i in range(m)] for _ in range(1)]
if m1 == 1:
    matrix = [[str(int(i+1)).ljust(3) for _ in range(1)] for i in range(n)]
for r in range(n):                                                 #[print(*r, sep='') for r in matrix]
    for c in range(m):
        print(matrix[r][c], end='')
    print()
