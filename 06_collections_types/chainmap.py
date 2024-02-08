import json
from collections import ChainMap, Counter
'''=================================================SUMMARY========================================================='''

def summary_1():
    numbers = {'one': 1, 'two': 2}
    letters = {'a': 'A', 'b': 'B'}
    chain_map_1 = ChainMap(numbers, letters)
    chain_map_2 = ChainMap.fromkeys(['one', 'two', 'three'])   #None
    chain_map_3 = ChainMap.fromkeys(['one', 'two', 'three'], -1)

'''=================================================TASK1========================================================='''

def zoo():
    with open("chainmap_unit/zoo.json", "r", encoding="utf-8") as input_file:
        return sum(ChainMap(*json.load(input_file)).values())

def mac(string):
    bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
    meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
    sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
    vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
    toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
    chain_map = ChainMap(bread, meat, sauce, vegetables, toppings)
    data = Counter(string.split(","))
    result = f"ИТОГ: {sum([v*chain_map[k] for k, v in data.items()])}р"
    answer = [f"{line[0].ljust(len(max(data.keys(), key=len)), ' ')} x {line[1]}" for line in sorted(data.most_common(), key=lambda line:line[0])]
    max_len = len(max([*answer, result], key=len))
    print("\n".join(answer))
    print(max_len*"-")
    return result
'''=================================================TASK2========================================================='''

def get_all_values(chainmap, key):
    answer = set()
    for line in chainmap.maps:
        try:
            answer.add(line[key])
        except:
            continue
    return answer

def deep_update(chainmap, key, value):
    a = set()
    for line in chainmap.maps:
        for k in line:
            a.add(k)
    if key in a:
        for line in chainmap.maps:
            if key in line:
                line[key] = value
            else:
                continue
    else:
        chainmap.maps[0].update({key:value})
    return None

def get_value(chainmap, key, from_left=True):
    a = set()
    for line in chainmap.maps:
        for k in line:
            a.add(k)
    if key in a:
        if from_left:
            for line in chainmap.maps:
                if key in line.keys():
                    return line[key]
        else:
            return chainmap.maps[-1][key]
    else:
        return None
