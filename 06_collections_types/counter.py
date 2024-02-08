from collections import Counter
import sys, csv, json
'''=================================================PART1========================================================='''
def first():
    files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
             'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
             'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
             'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
             'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
             'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
             'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
             'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
             'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
             'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
             'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
             'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
             'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
    a = Counter([item[item.index(".")+1:] for item in files])
    answer = "\n".join(sorted([f"{item}: {a[item]}" for item in a]))
    return answer

def count_occurences(word, words):
    ws = Counter([item.upper() for item in words.split()])
    return ws[word.upper()]

def third(string):
    my_list = Counter([item for item in string.split(",")])
    return "\n".join(sorted([f"{item}: {my_list[item]}" for item in my_list]))

def fouth(string):
    my_list = Counter([item for item in string.split(",")])
    max_len = len(max(my_list, key=len))
    answer = sorted([f"{item}{' '* (max_len- len(item))}: {sum([ord(i) if i != 'v ' else 0 for i in item])} UC "
                     f"x {my_list[item]} = {sum([ord(i) if i != ' ' else 0 for i in item]) * my_list[item]} UC" for item in my_list])

    return "\n".join(answer)

def zen_of_python():
    with open("counter_unit/pythonzen.txt", encoding="utf-8") as input_file:
        data = list(filter(lambda item: len(item), map(lambda line: line.strip().lower().split(), input_file.readlines())))
        answer = Counter()
        for line in data:
            answer.update(Counter("".join(line)))

    return "\n".join(sorted([f"{item}: {answer[item]}" for item in filter(lambda line: line.isalpha(), answer)]))


'''=================================================PART2========================================================='''

def pre():
    counter = Counter(green=10, red=25, blue=5)
    #print(counter.__dict__)  #{}
    #наделяем доп функционал
    counter.__dict__['min_value'] = lambda: min(counter.values())
    counter.max_value = lambda: max(counter.values())
    return True

def find_word_vol1(string):
    data = [line.lower() for line in string.split()]
    new_counter = Counter(data).most_common()[0][0]
    return new_counter


def find_word_vol2(string):
    new_counter = Counter([line.lower() for line in string.split()])
    new_counter.min_value = lambda:min(new_counter.values())
    total = filter(lambda item: item[1] == new_counter.min_value(), new_counter.most_common())
    return ", ".join(sorted([line[0] for line in total]))

def find_word_vol3(string):
    new_counter = Counter([line.lower() for line in string.split()])
    new_counter.max_value = lambda: max(new_counter.values())
    total = filter(lambda item: item[1] == new_counter.max_value(), new_counter.most_common())
    return sorted([line[0] for line in total], key=lambda item:item[0])[-1]

def statistic(string):
    new_counter = Counter([len(line.lower()) for line in string.split()])
    answer = [f"Слов длины {item[0]}: {item[1]}" for item in sorted(new_counter.most_common(), key=lambda line: line[1])]
    return "\n".join(answer)

def still_worthy():
    data = Counter({k:int(v) for k, v in [line.split() for line in sys.stdin]})
    return data.most_common()

def min_max():
    data = Counter(
        'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
    data.min_values = lambda: list(filter(lambda line: line[1] == min(data.values()), data.most_common()))
    data.max_values = lambda: list(filter(lambda line: line[1] == max(data.values()), data.most_common()))
    return data.max_values(), data.min_values()

def here_we_go_again():
    with open("counter_unit/name_log.csv", "r", encoding="utf-8") as input_file:
        data = Counter([line["email"] for line in csv.DictReader(input_file)])
    return "\n".join([f"{line[0]}: {line[1]}" for line in sorted(data.most_common(), key=lambda line: line[0])])

def scrabble(symbols, word):
    symbols_counter = Counter(symbols.lower())
    word_counter = Counter(word.lower())
    symbols_counter.subtract(word_counter)
    flag = True

    for line in symbols_counter.values():
        if line >= 0:
            continue
        else:
            flag = False
    return flag

def print_bar_chart(data, mark):
    new_data = Counter(data)
    max_len = len(max(new_data.keys(), key=len))
    # return "\n".join([f"{line[0]:{max_len}} |{line[1]*mark}" for line in new_data.most_common()])
    #OR
    # return "\n".join([f"{line[0].ljust(max_len, ' ')} |{line[1]*mark}" for line in new_data.most_common()])
    return max_len
print(print_bar_chart('beegeek', '+'))
languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print(print_bar_chart(languages, '#'))

def free_courses():
    with open("counter_unit/quarter1.csv", encoding="utf-8") as file1, \
        open("counter_unit/quarter2.csv", encoding="utf-8") as file2, \
        open("counter_unit/quarter3.csv", encoding="utf-8") as file3, \
        open("counter_unit/quarter4.csv", encoding="utf-8") as file4, \
        open("counter_unit/prices.json", encoding="utf-8") as prices:
        total_sum = 0
        q = Counter()
        price_list = json.load(prices)
        for file in [file1, file2, file3, file4]:
            q += Counter({k[0]: sum([price_list[k[0]]*int(i) for i in k[1:]]) for k in [line for line in csv.reader(file)][1:]})

        return q.total()

def free_courses_vol2():
    data = Counter(input().split())
    a_data = Counter({line:0 for line in data})
    for _ in range(int(input())):
        line = input().split()
        if line[0] in data.keys():
            a_data[line[0]] += int(line[1])
            data -= Counter({line[0]:1})
    return a_data.total()



