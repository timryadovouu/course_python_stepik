from collections import OrderedDict

# numbers1 = OrderedDict({'one': 1, 'two': 2, 'three': 3})
# numbers2 = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# numbers3 = OrderedDict(one=1, two=2, three=3)
# numbers4 = OrderedDict((['name', 'Timur'], ['surname', 'Guev'], ['hobby', 'math']))

def reversed_dict():
    data = OrderedDict(key1='value1', key2='value2', key3='value3')
    new_dict = OrderedDict([(item, data[item]) for item in reversed(data)])
    return new_dict
def first_last_etc():
    data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4', key5='value5', key6='value6')
    a = []
    for i in range(0, len(data) // 2):
        a.append((list(data)[i], data[list(data)[i]]))
        a.append((list(data)[len(data)-1-i], data[list(data)[len(data)-1-i]]))
    return OrderedDict(a)

def custom_sort(ordered_dict, by_values=False):
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict.items(), key=lambda item:item[1]):
            ordered_dict.move_to_end(key[0])
    return ordered_dict

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data, True)
print(data)