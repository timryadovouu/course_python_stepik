def timur_and_new_course(my_list):           #2_1
    #my_list = [int(input()) for _ in range(3)]
    prohod_1 = sum(my_list)
    prohod_2 = 2 * min(my_list) + 2 * (prohod_1 - min(my_list) - max(my_list))
    return min(prohod_1, prohod_2)

my_list = [input() for _ in range(3)]

def similar_letters(my_list):              #2_2
    #my_list = [input() for _ in range(3)]
    ru = [ord(chr(i)) for i in range(ord("а"), ord("я"))] + [ord(chr(i)) for i in range(ord("А"), ord("Я"))]
    en = [ord(chr(i)) for i in range(ord("a"), ord("z"))] + [ord(chr(i)) for i in range(ord("A"), ord("Z"))]
    answer = ["1" if ord(c) in ru else "2" for c in my_list]
    if "".join(answer) == "222":
        return "en"
    elif "".join(answer) == "111":
        return "ru"
    else:
        return "mix"

def perevorator(new_list):                   #2_3
    #new_list = input().split()
    n, x, y, a, b = int(new_list[0]), int(new_list[1]), int(new_list[2]), int(new_list[3]), int(new_list[4])
    n_list = [int(i + 1) for i in range(n)]
    n_list[x - 1:y] = n_list[x - 1:y][::-1]
    n_list[a - 1:b] = n_list[a - 1:b][::-1]
    return " ".join(map(str, n_list))

def out_if_more_than_one(new_list):            #2_4
    #new_list = input().split()
    result, a = {}, []
    for num in new_list: result[num] = result.get(num, 0) + 1
    for value, key in result.items():
        if key != 1: a.append(int(value))
    return " ".join(map(str, sorted(a)))

def max_group(new_list):                #2_5
    list_sum = [sum(map(int, list(str(num)))) for num in new_list]
    result = {}
    for value in list_sum: result[value] = result.get(value, 0) + 1
    return max(result.values())
print(max_group([int(_+1) for _ in range(int(input()))]))

def difficulty_of_translation(my_list):           #2_6
    #my_list = [input().split(", ") for _ in range(int(input()))]
    answer, a = {}, []
    for pod in my_list:
        for lang in pod:
            answer[lang] = answer.get(lang, 0) + 1
    for key, value in answer.items():
        if n == value: a.append(key)
    if a:
        return "\n".join(sorted(a))
    else:
        return "Сериал снять не удастся"

glasn = "а, у, о, ы, и, э, я, ю, ё, е".replace(", ", "")
def zamena(s):                            #2_7
    for char in s:
        if char in glasn:
            s = s.replace(char, "1")
        else:
            s = s.replace(char, "0")
    return int(s[::-1])
def similar_words(word, my_list):
    #word, my_list = input(), [input() for _ in range(int(input()))]
    a, new_word = [zamena(my_list[i]) for i in range(len(my_list))], zamena(word)
    total = [my_list[i] for i in range(len(my_list)) if new_word == a[i]]
    return "\n".join(total)


# exist_list = [input().replace("@beegeek.bzz", '') for _ in range(int(input()))]     #2_8
# new_list = [input() for _ in range(int(input()))]
# n_exist_list, answer, hah = [], {}, []
# def find_num(s):
#     for char in s:
#         if char in " 1234567890":
#             return s.index(char)
# def prov(s):
#     if find_num(s):
#         return find_num(s)
#     else:
#         return len(s)
# for item in exist_list:
#     s = ""
#     for char in item:
#         if char in "0123456789":
#             s += char
#     hah.append(item[:prov(item)])
#     if s:
#         n_exist_list.append(s)
#     else:
#         n_exist_list.append("")
# for i in hah:
#     answer[i] = [[], [''] + [str(i + 1) for i in range(15)]]
# for key in answer.keys():
#     a = []
#     for i in range(len(hah)):
#         if hah[i] == key:
#             a.append(n_exist_list[i])
#     answer[key] = [a, [''] + [str(i + 1) for i in range(15)]]
# numbers = [''] + [str(i + 1) for i in range(20)]
# m_numbers = [[''] + [str(i + 1) for i in range(20)] for _ in range(len(hah))]
# for item in new_list:
#     if item in answer.keys():
#         length = len(answer[item][0])
#         if sorted(answer[item][0]) == sorted(answer[item][1][:length]):
#             print(item + answer[item][1][length] + "@beegeek.bzz")
#             answer[item][0].append(answer[item][1][length])
#             answer[item][1] = [i for i in answer[item][1] if i not in answer[item][0]]
#         else:
#             print(item + answer[item][1][0] + "@beegeek.bzz")
#             answer[item][0].append(answer[item][1][0])
#             answer[item][1] = [i for i in answer[item][1] if i not in answer[item][0]]
#     else:
#         print(item + "@beegeek.bzz")
#         answer[item] = ['']



# from math import *                                             #2_9
# from datetime import datetime
# with open('files.txt', encoding='utf-8') as in_file:
#     my_list = list(map(lambda line: line.strip().split(), in_file.readlines()))
#     my_dict = {}
#     for item in my_list:
#         ind = item[0].index(".")
#         file_extension = item[0][ind+1:]
#         my_dict.setdefault(file_extension)
#
#     for key in my_dict:
#         fe = []
#         fv = []
#         fv_d = {}
#         for item in my_list:
#             ind = item[0].index(".")
#             if key == item[0][ind+1:]:
#                 fe.append(item[0])
#                 item[1] = int(item[1])
#                 if item[2] == "KB":
#                     item[1] *= 1024
#                 if item[2] == "MB":
#                     item[1] *= 1024**2
#                 if item[2] == "GB":
#                     item[1] *= 1024**3
#                 fv.append(item[1])
#         summa = sum(fv)
#         # print(fv)
#         f_ex =["B", "KB", "MB", "GB"]
#         b_ind = 0
#         while summa // 1024 != 0:
#             summa /= 1024
#             b_ind += 1
#         my_dict[key] = fe, round(summa), b_ind
# out_file = open('ou.txt', 'w', encoding='utf-8')
# for key in dict(sorted(my_dict.items())):
#     for item in sorted(my_dict[key][0]):
#         print(item)
#         out_file.write(f"{item}\n")
#     print("----------", f"Summary: {my_dict[key][1]} {f_ex[my_dict[key][2]]}","", sep='\n')
#     x = ["----------\n", f"Summary: {my_dict[key][1]} {f_ex[my_dict[key][2]]}\n","\n"]
#     out_file.writelines(x)
# out_file.close()






























