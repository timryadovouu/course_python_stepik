def hide_card(card_number):              #1_1
    return "*"*12 + card_number.replace(" ", "")[-4:]
def same_parity(numbers):                 #1_2
    return list(filter(lambda x: x%2 == numbers[0] % 2 , numbers))
def is_valid(string):                     #1_3
    return string.isdigit() and len(string) in [4, 5, 6]
def print_given(*args, **kwargs):          #1_4
    for value in args:
        print(f'{value} {type(value)}')
    for key, value in sorted(dict(kwargs).items()):
        print(f'{key} {value} {type(value)}')
def convert(string):                                    #1_5
    counter1, counter2 = 0, 0
    for c in string:
        if ord(c) in range(ord('a'), ord('z')+1):
            counter1 += 1
        elif ord(c) in range(ord('A'), ord('Z')+1):
            counter2 += 1
    if counter1 >= counter2:
        return str(string).lower()
    else:
        return str(string).upper()
def filter_anagrams(word, words):                  #1_6
    answer = []
    new_words = [''.join(sorted(list(i))) for i in words]
    word_massive = ''.join(sorted(list(word)))
    for i in range(len(new_words)):
        if new_words[i] == word_massive:
            answer.append(words[i])
    return answer
def likes(names):                  #1_7
    if len(names) == 0 : return "Никто не оценил данную запись"
    if len(names) == 1 : return f"{names[0]} оценил(а) данную запись"
    if len(names) == 2: return f"{names[0]} и {names[1]} оценили данную запись"
    if len(names) == 3: return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    return f"{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись"
def index_of_nearest(numbers, number):      #1_8
    if len(numbers) == 0: return -1
    min_epsilon = abs(number - numbers[0])
    index = 0
    for i in range(len(numbers)):
        epsilon = abs(number - numbers[i])
        if epsilon < min_epsilon:
            min_epsilon = epsilon
            index = i
    return index
def spell(*words):          #1_9
    new_words = sorted([item.lower() for item in words], key=len, reverse=True)
    my_dict = {}
    for item in words:
        if item[0].lower() not in my_dict:
            my_dict[item[0].lower()] = len(item)
        elif len(item) >  my_dict[item[0].lower()] : my_dict[item[0].lower()] = len(item)
    return my_dict
    #return {item[0].lower() : len(item) for item in sorted(words, key=len)}
def choose_plural(amount, declensions):              #1_10
    okonchanie = amount % 10
    okonchanie_1 = amount % 100
    if okonchanie in range(2, 5) and okonchanie_1 not in range(11, 15): return f"{amount} {declensions[1]}" #примера
    elif okonchanie == 1 and okonchanie_1 not in range(11, 15): return f"{amount} {declensions[0]}" #пример
    elif okonchanie_1 in range(11, 15): return f"{amount} {declensions[2]}"          #примеров
    else: return f"{amount} {declensions[2]}"
def get_biggest(numbers):                   #1_11
    if len(numbers) == 0: return -1
    new_numbers = sorted(numbers, key = lambda x: str(x)*len(str(max(numbers))), reverse=True)
    new_numbers = int(''.join(map(str, new_numbers)))
    return new_numbers