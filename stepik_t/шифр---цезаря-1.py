print('-----Добро пожаловать!-----')

lower_eng_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # 26
upper_eng_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lower_rus_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]  # 32
upper_rus_alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

what_we_are_suppose_to_do = input('Дешифровка(д) или шифровка(ш)? ')
while what_we_are_suppose_to_do !='д' and what_we_are_suppose_to_do !='ш':
    what_we_are_suppose_to_do = input('Ты тупой? д или ш ')
language = input('Какой язык выбираешь? Английский(а) -- Русский(р) ')
while language != 'а' and language != 'р':
    language = input('Видать дурак а или р ')
n = input('Какой сдвиг? ')
while n.isdigit() != True:
    n = input('введи число ')
message = input('Введите текст ')
while message.isspace() == True:
    message = input('Введите текст ')

if language == 'р':
    moshnost = len(lower_rus_alphabet)
    low_alphabet = lower_rus_alphabet
    up_alphabet = upper_rus_alphabet
if language == 'а':
    moshnost = len(lower_eng_alphabet)
    low_alphabet = lower_eng_alphabet
    up_alphabet = upper_eng_alphabet

def bill_shifr(direction, step, text):
        global place, index
        my_list = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].lower():
                    place = low_alphabet.index(text[i])
                if text[i] == text[i].upper():
                    place = up_alphabet.index(text[i])
                if direction == 'ш':
                    index = (place + step) % moshnost
                if direction == 'д':
                    index = (place - step) % moshnost
                if text[i] == text[i].lower():
                    my_list += low_alphabet[index]
                if text[i] == text[i].upper():
                    my_list += up_alphabet[index]
            else:
                my_list += text[i]
        print(my_list)

bill_shifr(what_we_are_suppose_to_do, int(n), message)






