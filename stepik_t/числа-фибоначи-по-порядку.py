n = int(input())
a1 = 0
a2 = 1
s = ''
sum = 0

for i in range(n):
    a1, a2 = a2, a1 + a2
    sum += a1
    print(a1, end=' ')


