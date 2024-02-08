
lower_eng_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # 26
upper_eng_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lower_rus_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]  # 32
upper_rus_alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]


message = input()
while message.isspace() == True:
    message = input('Введите текст: ')


moshnost = len(lower_eng_alphabet)
low_alphabet = lower_eng_alphabet
up_alphabet = upper_eng_alphabet

def bill_shifr(text):
    global place, index                   #my name is Python!
    my_list_0 = text.split(' ')
    empty_sp, empty_str = [], ''
    s, w, counter = text.split(), [], 0    #считаем длину слов правильную
    l = [int(len(i)) for i in s]  # считаем длину слов неправильную
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j].isalpha():
                counter += 1
            else:
                continue
        w.append(counter)
        counter = 0
    for j in range(len(my_list_0)):
        for i in range(len(my_list_0[j])):
            if my_list_0[j][i].isalpha():
                if my_list_0[j][i] == my_list_0[j][i].lower():
                    place = low_alphabet.index(my_list_0[j][i])
                    index = (place + int(w[j])) % moshnost
                if my_list_0[j][i] == my_list_0[j][i].upper():
                    place = up_alphabet.index(my_list_0[j][i])
                    index = (place + int(w[j])) % moshnost

                if my_list_0[j][i] == my_list_0[j][i].lower():
                    empty_str += low_alphabet[index]
                if my_list_0[j][i] == my_list_0[j][i].upper():
                    empty_str += up_alphabet[index]
            else:
                empty_str += my_list_0[j][i]
    for k in l:
        st = empty_str[0:k]
        empty_sp.append(st)
        empty_str = empty_str[k:]

    print(*empty_sp)

bill_shifr(message)









