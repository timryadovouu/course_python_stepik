s = input()
my_list, letter = [], chr(ord('а'))         #роскомнадзор
my_list.append(s)
my_list = my_list + ['запретил', 'букву']
msh = 1
leng = 0
ss = s + 'запретил' + 'букву'
for i in range(1,len(ss)):
    if ss[i-1] != ss[i]:
        leng += 1
while leng != 0:
    if letter in my_list[0] or letter in my_list[1] or letter in my_list[2]:
        s = ' '.join(my_list + [letter])
        s = s.replace('  ', ' ')
        s = s.replace('  ', ' ')
        print(s.strip())
    for i in range(len(my_list)):
        index_letter = my_list[i].find(letter)
        while index_letter != -1:
            my_list[i] = my_list[i][:index_letter] + my_list[i][index_letter+1:]
            index_letter = my_list[i].find(letter)
    letter = chr(ord('а') + msh)
    msh += 1
    if len(my_list[0]) != leng and len(my_list[1]) != leng and len(my_list[2]) != leng:
        leng -= 1
    else:
        continue
'''s = input() + ' запретил букву'
for c in 'абвгджезийклмнопрстуфхчшщьыъэюя':
    if c in s:
        print(s, c)
        s = s.replace(c,'').strip().replace('  ', ' ')'''



