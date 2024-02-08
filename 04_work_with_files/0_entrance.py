import sys
from datetime import datetime


# for line in sys.stdin:
#     print(line.strip("\n"))

# data = [line.strip("") for line in sys.stdin]    тоже самое  # data = list(map(str.strip, sys.stdin))
# data1 = sys.stdin.read()
# print(data1)
# sys.stdout.write("hello, world!")

# temp = sys.stdout
# sys.stdout = open('log.txt', 'w')
# print('testing123')
# print('another line')
# sys.stdout.close()
# sys.stdout = temp
# print('back to normal')

def backwards_out():                                                      #1_1
    data = [line.strip("\n")[::-1] for line in sys.stdin]
    return "\n".join(data)

def difference_btw_dates():                                                #1_2
    data = [datetime.strptime(line.strip("\n"), "%Y-%m-%d") for line in sys.stdin]
    return (max(data) - min(data)).days

def lemma_about_three_socks():                                        #1_3
    data = [int(line.strip("\n")) for line in sys.stdin]
    print(len(data))
    if (len(data)%2 == 0) == (data[-1]%2==0):
        return "Дима"
    else:
        return "Анри"

def tall_of_students():                                              #1_4
    data = [int(line.strip("\n")) for line in sys.stdin]
    if len(data) == 0: return "нет учеников"
    else:
        average = sum(data)/len(data)
        return "\n".join((f"Рост самого низкого ученика: {min(data)}",
                          f"Рост самого высокого ученика: {max(data)}",
                          f"Средний рост: {average}"))

def find_comments():                                                         #1_5
    data = [line.strip("\n").lstrip() for line in sys.stdin]
    total = [1 for line in data if line[0] == "#"]
    return sum(total)

def delete_comments():                                                        #1_6
    q = []
    for line in [line.strip("\n") for line in sys.stdin]:
        if line:
            if line.lstrip()[0] != "#":
                q.append(line)
        else: q.append("")
    return "\n".join(q)

def real_news():                                                            #1_7
    news = [[line.strip() for line in line.strip("\n").split("/")] for line in sys.stdin]
    otbor = [line for line in news[0:len(news)-1] if line[1] == "".join(news[-1])]
    return "\n".join([line[0] for line in sorted(otbor, key=lambda line: (line[2], line[0]))])

def dates_in_order():                                    #1_8
    dates, result = [datetime.strptime(line.strip("\n"), "%d.%m.%Y") for line in sys.stdin], {}
    for value in dates: result[value] = result.get(value, 0) + 1
    if dates == sorted(dates) and len(dates) == len(result):
        return "ASC"
    elif dates == sorted(dates, reverse=True) and len(dates) == len(result):
        return "DESC"
    else:
        return "MIX"

def is_progression():                       #1_9
    numbers = [int(line.strip("\n")) for line in sys.stdin]
    d, q = numbers[1] - numbers[0], numbers[1]/numbers[0]
    if sum(numbers) == (2*numbers[0] + d*(len(numbers)-1))*len(numbers)/2:
        return "Арифметическая прогрессия"
    elif sum(numbers) == numbers[0]*(1-q**len(numbers)) / (1-q):
        return "Геометрическая прогрессия"
    else:
        return "Не прогрессия"

