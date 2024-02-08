n = int(input())
my_list, my_list1, s, itog = [], [], '', ''

for i in range(n):
    s = input()
    my_list.append(s)

k = int(input())

for i in range(0, len(my_list)):
    s = my_list[i]
    if len(s) < k:
        continue
    itog += s[k-1]
    s = ''

print(itog)


