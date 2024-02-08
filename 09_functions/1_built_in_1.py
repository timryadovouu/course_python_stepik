'''===================================================SUMMARY======================================================='''
'''===================================================SUMMARY======================================================='''
def foo():
    print(round(3.4445, ))
    print(pow(2, 5, 30))   #Функция возвращает число base в степени exp, с опциональным делением с остатком на mod
    print(int('111', base=2))
    print(complex(4, 9))
    print(complex('11+5j'))
    print(bool('Beegeek'))              #True
    print(bool([]))                     #False
    #dict
    print(dict(a=1, b=2))
    print(dict([('a', 1), ('b', 2), ('c', 3)]))
    print(dict([('a', 1), ('b', 2)], c=3, d=4))

    print(min([], default='Empty'))  #default — значение по умолчанию, если итерируемый объект окажется пустым
    #Функция all() возвращает значение True, если все элементы в итерируемом объекте истинны
    print(all([1, 2, 3]))          #true
    print(all([1, 2, 3, 0, 5]))      #false
    #Функция any() возвращает True, если какой-либо (любой) элемент в итерируемом объекте является истинным
    print(isinstance(3.5, (float, int, str)))  #можно кортеж
    def bar():
        colors = ['redd', 'greenn', 'bluee']
        for pair in enumerate(colors, 1):
            print(pair)
    def rangee():
        my_range = range(1, 11)
        print(my_range[0])
        print(my_range[1:4])
        print(my_range.count(7))
        print(my_range.index(10))
        print(my_range == range(1, 10))
        # 1
        # range(2, 5)
        # 1
        # 9
        # False
    def zipp():
        numbers = [1, 2, 3]
        words = ['one', 'two', 'three']
        romans = ['I', 'II', 'III']
        for number in zip(numbers, words, romans):
            print(number)
    return True

'''===================================================TASKS======================================================='''

# [print(chr(i)) for i in range(ord("a"), ord("z")+1)]

def convert(number):
    return (bin(number)[:bin(number).index("b")-1] + bin(number)[bin(number).index("b")+1:],
            oct(number)[:oct(number).index("o")-1] + oct(number)[oct(number).index("o")+1:],
            hex(number)[:hex(number).index("x")-1] + hex(number)[hex(number).index("x")+1:])
# print(convert(-24))


def worst_film():
    films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
             'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
            'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
            'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
            'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
            'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
            'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
            'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
            'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
            'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
            'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
    print(min(films.items(), key=lambda line: (sum([l for l in line[1].values()]))/ len(line[1]))[0])

def non_negative_even(numbers):
    if list(filter(lambda line: line%2==0 and line >= 0, numbers)) == numbers:
        return True
    return False
    # print(non_negative_even([0, 2, 4, 8, 16]))
    # print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
    # print(non_negative_even([0, 0, 0, 0, 0]))

def is_greater(lists, number):
    data = [sum(line) > number for line in lists]
    return any(data)

def custom_isinstance(objects, typeinfo):
    data = [1 if isinstance(item, typeinfo) else 0 for item in objects]
    return sum(data)

def my_pow(number):
    return sum([int(pair[1])**pair[0] for pair in enumerate(str(number), 1)])


def zip_longest(*args, fill = None):
    max_len = len(max(args, key=len))
    for item in args:
        if len(item) < max_len:
            for _ in range(max_len-len(item)):
                item.append(fill)
        else:
            continue
    return [line for line in zip(*args)]
    # print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

def unusual_sort(string):
    letters = list(filter(lambda line: line.isalpha(), list(string)))
    numbers = list(map(int, (filter(lambda line: line.isdigit(), list(string)))))
    low_letters, up_letters, even_numbers, odd_numbers = list(filter(lambda line: line.islower(), letters)),\
        list(filter(lambda line: line.isupper(), letters)), \
        list(filter(lambda line: line%2 == 0, numbers)),\
        list(filter(lambda line: line%2 == 1, numbers))
    answer = f"{''.join(sorted(low_letters))}{''.join(sorted(up_letters))}{''.join(sorted(map(str, odd_numbers)))}{''.join(sorted(map(str,even_numbers)))}"
    return answer

