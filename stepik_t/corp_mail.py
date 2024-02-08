#https://github.com/python-generation/Professional/blob/main/Module_2/Module_2.2/Module_2.2.8/input.txt
#https://stepik.org/lesson/569749/step/8?unit=564263

exist_list = [input().replace("@beegeek.bzz", '') for _ in range(int(input()))]
new_list = [input() for _ in range(int(input()))]
n_exist_list, answer, hah = [], {}, []
def find_num(s):
    for char in s:
        if char in " 1234567890":
            return s.index(char)
def prov(s):
    if find_num(s):
        return find_num(s)
    else:
        return len(s)

for item in exist_list:
    s = ""
    for char in item:
        if char in "0123456789":
            s += char
    hah.append(item[:prov(item)])
    if s:
        n_exist_list.append(s)
    else:
        n_exist_list.append("")
for i in hah:
    answer[i] = [[], [''] + [str(i + 1) for i in range(15)]]
for key in answer.keys():
    a = []
    for i in range(len(hah)):
        if hah[i] == key:
            a.append(n_exist_list[i])
    answer[key] = [a, [''] + [str(i + 1) for i in range(15)]]

print(f"Исходник :: {exist_list}",
      f"Кому добавить :: {new_list}",
      f"Индексы у исходников :: {n_exist_list}",
      f"Исходник без индексов :: {hah}",
      f"Словарик ::  {answer}", sep='\n')
print()
numbers = [''] + [str(i + 1) for i in range(20)]
m_numbers = [[''] + [str(i + 1) for i in range(20)] for _ in range(len(hah))]
for item in new_list:
    if item in answer.keys():
        length = len(answer[item][0])
        if sorted(answer[item][0]) == sorted(answer[item][1][:length]):
            print(item + answer[item][1][length] + "@beegeek.bzz")
            answer[item][0].append(answer[item][1][length])
            answer[item][1] = [i for i in answer[item][1] if i not in answer[item][0]]
        else:
            print(item + answer[item][1][0] + "@beegeek.bzz")
            answer[item][0].append(answer[item][1][0])
            answer[item][1] = [i for i in answer[item][1] if i not in answer[item][0]]

    else:
        print(item + "@beegeek.bzz")
        answer[item] = ['']

print()
print(f"Конечный словарь ::  {answer}")
