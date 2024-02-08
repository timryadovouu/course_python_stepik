import json, sys, csv
from datetime import datetime


'''==============================================SUMMARY================================================'''
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
#
# json_data = json.dumps(data, indent="", sort_keys=False, separators=(",", ": "), skipkeys=True)  # сериализуем словарь data в json строку
# print(json_data)
# with open('countries_1.json', 'w') as file:                                         #запись в файл
#     json.dump(data, file)
# print()
# json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'  #десериализация
# data = json.loads(json_data)
# print(data)
# print()
# with open('data.json') as file:
#     data = json.load(file)                # передаем файловый объект
#     for key, value in data.items():
#         if type(value) == list:
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')

'''==============================================TASKS================================================'''
def first_one():
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
    json_data = json.dumps(countries, indent="   ", sort_keys=True, separators=(",", " - "), skipkeys=True)
    return json_data

def second_one():
    words = {
        frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
        "travel": "trævl",
        ("hello", "world"): ("həˈləʊ", "wɜːld"),
        "moonlight": "muːn.laɪt",
        "sunshine": "ˈsʌn.ʃaɪn",
        ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
        "adventure": "ədˈventʃər",
        "beautiful": "ˈbjuːtɪfl",
        frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
        "bicycle": "baisikl",
        ("pilot", "fly"): ("pailət", "flai")
    }
    data_json = json.dumps(words, skipkeys=True)
    return data_json

def third_one():
    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
    with open('json_unit/data_0.json', 'w') as file:
        json.dump([club1, club2, club3], file, indent="   ")
third_one()
def fouth_one():
    specs = {
             'Модель': 'AMD Ryzen 5 5600G',
             'Год релиза': 2021,
             'Сокет': 'AM4',
             'Техпроцесс': '7 нм',
             'Ядро': 'Cezanne',
             'Объем кэша L2': '3 МБ',
             'Объем кэша L3': '16 МБ',
             'Базовая частота': '3900 МГц'
            }
    specs_json = json.dumps(specs, ensure_ascii=False, indent="   ")
    return specs_json

def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False

def correct_json():
    data = json.loads(sys.stdin.read())
    for key, value in data.items():
        if type(value) == list:
            print(f"{key}: {', '.join(map(str, value))}")
        else:
            print(f"{key}: {value}")
    return True

def different_types():
    with open("json_unit/data.json", "r", encoding="utf-8") as input_file,\
            open("json_unit/updated_data.json", "w", encoding="utf-8") as output_file:
        data = json.load(input_file)
        new = []
        for ind_i in range(len(data)):
            if data[ind_i] is not None:
                new.append(data[ind_i])
            else: continue
        for ind_i in range(len(new)):
            if type(new[ind_i]) == str:
                new[ind_i] += "!"
            elif type(new[ind_i]) == int:
                new[ind_i] += 1
            elif type(new[ind_i]) == bool:
                new[ind_i] = not new[ind_i]
            elif type(new[ind_i]) == list:
                new[ind_i] += new[ind_i]
            elif type(new[ind_i]) == dict:
                new[ind_i].update({"newkey": None})
        json.dump(new, output_file, indent="   ")
        return True
def merge_json_files():
    with open("json_unit/data1.json", "r", encoding="utf-8") as input_file_1, \
            open("json_unit/data2.json", "r", encoding="utf-8") as input_file_2, \
                open("json_unit/data_merge.json", "w", encoding="utf-8") as output_file:
        data1, data2 = json.load(input_file_1), json.load(input_file_2)
        update_data = data1 | data2
        json.dump(update_data, output_file, sort_keys=True, indent="   ")
        return True

def recover_missing_keys():
    with open("json_unit/people.json", "r", encoding="utf-8") as input_file, \
        open("json_unit/updated_people.json", "w", encoding="utf-8") as output_file:
        data = json.load(input_file)
        all_keys = {key for key in data[0].keys()}
        for line in data[1:]:
            all_keys |= {key for key in line.keys()}
        for ind in range(len(data)):
            for key in all_keys:
                if key not in data[ind]:
                    data[ind] |= {key:None}
        json.dump(data, output_file, sort_keys=True, indent="   ")
        return True

def religions():
    with open("json_unit/countries_1.json", "r", encoding="utf-8") as input_file, \
        open("json_unit/religion.json", "w", encoding="utf-8") as output_file:
        data = json.load(input_file)
        dict_names = {}
        for line in data:
            dict_names.setdefault(line["religion"], []).append(line["country"])
        json.dump(dict_names, output_file, indent="   ")
        return True

def sport_playgrounds():
    with open("json_unit/playgrounds.csv", "r", encoding="utf-8") as input_file, \
        open("json_unit/addresses.json", "w", encoding="utf-8") as output_file:
        data = [line for line in csv.DictReader(input_file, delimiter =";")]
        total_dict = {}
        for line in data:
            total_dict.setdefault(line["AdmArea"], {}).setdefault(line["District"], []).append(line["Address"])
        json.dump(total_dict, output_file, indent="   ", ensure_ascii=False)
        return True

def students_of_the_course():
    with open("json_unit/students.json", "r", encoding="utf-8") as input_file, \
        open("json_unit/data.csv", "w", encoding="utf-8", newline="") as output_file:
        new_data = filter(lambda line: line["progress"] >= 75 and line["age"] >= 18, json.load(input_file))
        total = sorted([[line["name"], line["phone"]] for line in new_data])
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(["name", "phone"])
        for row in total:
            writer.writerow(row)
        return True

def pools():
    with open("json_unit/pools.json", "r", encoding="utf-8") as input_file:
        new_data = filter(lambda line: datetime.strptime(line["WorkingHoursSummer"]["Понедельник"][0:5], "%H:%M").hour <= 10 and \
                          datetime.strptime(line["WorkingHoursSummer"]["Понедельник"][-5:], "%H:%M").hour >= 12, json.load(input_file))
        max_length = max(new_data, key=lambda line: (line["DimensionsSummer"]["Length"], line["DimensionsSummer"]["Width"]))
        answer = [f"{max_length['DimensionsSummer']['Length']}x{max_length['DimensionsSummer']['Width']}",\
                  max_length["Address"]]
        return "\n".join(answer)

def exam_results():
    with open("json_unit/exam_results.csv", "r", encoding="utf-8") as input_file, \
        open("json_unit/best_scores.json", "w", encoding="utf-8", newline="") as output_file:
        data = csv.DictReader(input_file, delimiter=",")
        data.fieldnames[2] = 'best_score'
        new_dict, total = {}, []
        for line in [line for line in data]:
            new_dict.setdefault(line["email"], []).append(line)
        for key in new_dict.keys():
            pre = sorted(new_dict[key], key=lambda q: (int(q["best_score"]),datetime.strptime(q["date_and_time"], "%Y-%m-%d %H:%M:%S")), reverse=True)[0]
            pre["best_score"] = int(pre["best_score"])
            total.append(pre)
        json.dump(sorted(total, key=lambda line: line["email"]), output_file, indent="   ")
        return True


def catering_vol1():
    with open("json_unit/food_services.json", "r", encoding="utf-8") as input_file:
        district_dict, cafe_dict = {}, {}
        for line in json.load(input_file):
            district_dict[line["District"]] = district_dict.get(line["District"], 0) + 1
            if line["IsNetObject"] == "да":
                cafe_dict[line["OperatingCompany"]] = cafe_dict.get(line["OperatingCompany"], 0) + 1
        district_ans = sorted(district_dict.items(), key= lambda line: line[1], reverse=True)[0]
        cafe_ans = sorted(cafe_dict.items(), key= lambda line: line[1], reverse=True)[0]
        total = [f"{district_ans[0]}: {district_ans[1]}", f"{cafe_ans[0]}: {cafe_ans[1]}"]
        return "\n".join(total)

def catering_vol2():
    with open("json_unit/food_services.json", "r", encoding="utf-8") as input_file:
        new_dict, total = {}, []
        for line in json.load(input_file):
            new_dict.setdefault(line["TypeObject"], []).append((line["Name"],line["SeatsCount"]))
        for key in sorted(new_dict.keys()):
            total.append(f"{key}: {sorted(new_dict[key], key=lambda line:line[1], reverse=True)[0][0]}, {sorted(new_dict[key], key=lambda line:line[1], reverse=True)[0][1]}")
        return "\n".join(total)

