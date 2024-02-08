import random
word_list = ['КЛЮЧ', 'КНИГА']
def get_word():
    word = random.choice(word_list)
    return word.upper()
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    word_completion = ['_' for i in range(len(word))]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(*word_completion)

    while guessed == False and tries > 0:
        vvod = input('Введи букву или слово: ').upper()
        if len(vvod) == 1 and vvod.isalpha():
            if vvod in guessed_letters:
                print(f'ВЫ УЖЕ НАЗЫВАЛИ БУКВУ {vvod} ----- ОСТАЛОСЬ {tries} ПОПЫТОК')
            elif vvod not in word:
                tries -= 1
                print(f'ТАКОЙ БУКВЫ УВЫ НЕТ ----- ОСТАЛОСЬ {tries} ПОПЫТОК')
                print(display_hangman(tries))
                print(*word_completion)
                guessed_letters.append(vvod)
            else:
                print(f'ОТЛИЧНО! БУКВА  ..{vvod}..  ПРИСУТСВУЕТ ----- ОСТАЛОСЬ {tries} ПОПЫТОК')
                print(display_hangman(tries))
                guessed_letters.append(vvod)
                for i in range(len(word)):
                    index = word.index(vvod)
                    word_completion[index] = vvod
                print(*word_completion)
                if '_' not in word_completion:
                    guessed = True
                    print('ВЫ УГАДАЛИ!')
        elif len(vvod) == len(word) and vvod.isalpha():
            if vvod in guessed_words:
                print(f'ВЫ УЖЕ НАЗЫВАЛИ {vvod}')
            elif vvod != word:
                tries -= 1
                print(f'ТАКОГО СЛОВА УВЫ НЕТ ----- ОСТАЛОСЬ {tries} ПОПЫТОК')
                print(display_hangman(tries))
                print(*word_completion)
                guessed_words.append(vvod)
            else:
                guessed = True
                print('ВЫ УГАДАЛИ!')
        if tries == 0:
            print(f'НЕ РАССТРАИВАЙСЯ! ЗАГАДАННЫМ СЛОВОМ БЫЛО {word}')

play(get_word())
answer = input('ХОЧЕШЬ СЫГРАТЬ ЕЩЕ?  д=да ')
if answer == 'д':
    play(get_word())
else:
    print('НУ ПОКА ПЕТУШОК')

