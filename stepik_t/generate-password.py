import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

how_many = input('Сколько паролей ты хочешь?')
how_long = input('Какой длины?')

first = input('Включать ли цифры 0123456789?')
second = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
third = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
forth = input('Включать ли символы !#$%&*+-=?@^_?')
fifth = input('Исключать ли неоднозначные символы il1Lo0O?')

if first == 'y' or first == 'д':
    chars += digits
if second == 'y' or second == 'д':
    chars += lowercase_letters
if third == 'y' or third == 'д':
    chars += uppercase_letters
if forth == 'y' or forth == 'д':
    chars += punctuation
if fifth == 'y' or fifth == 'д':
    for c in 'il1Lo0O':
        chars.replace(c, '')
def generate_password(length, chars):
    return random.sample(chars,length)

for _ in range(int(how_many)):
    print(''.join(generate_password(int(how_long), chars)))