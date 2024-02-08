import csv_unit, time
from datetime import datetime
'''==============================================READ================================================'''

with open("csv_unit/products.csv", encoding='utf-8') as file:
    #data = file.read()
    # table = [r.split(',') for r in data.splitlines()]                                #1ый способ чтения
    # del table[0]
    # table.sort(key=lambda item: int(item[1]))

    table_copy = csv_unit.reader(file, delimiter =';', quotechar ='"')                       #2ой способ
    # [print(row) for row in table_copy]
    # for keywords, price, product_name in table_copy:
    #     print(f'Ключевые слова: {keywords}, цена: {price}, название: {product_name}')
    # for index, row in enumerate(table_copy):
    #     if index > 5:
    #         break
    #     print(row)

    # rows = csv_unit.DictReader(file, delimiter=';', quotechar='"')                               #3ий способ
    # most_expensive = sorted(rows, key=lambda item: int(item["price"]), reverse=True)

'''==============================================WRITE================================================'''

with open('csv_unit/students.csv', 'w', encoding='utf-8', newline='') as file:
    #1ый способ
    columns = ['first_name', 'second_name', 'class_number', 'class_letter']
    #data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]
    # writer = csv_unit.writer(file)
    # writer = csv_unit.writer(file, delimiter=';', quoting=csv_unit.QUOTE_NONNUMERIC)    #quoting=csv_unit.QUOTE_NONNUMERIC ==> все нечисловые значения в кавычки
    # writer.writerow(columns)                 # запись заголовков
    # for row in data:                         # запись строк или writer.writerows(data)
    #     writer.writerow(row)

    #2ой способ
    # data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
    #         {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
    #         {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]
    # columns = ['first_name', 'second_name', 'class_number', 'class_letter']
    #
    # writer = csv_unit.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv_unit.QUOTE_NONNUMERIC)
    # writer.writeheader()                # запись заголовков
    # for row in data:                    # запись строк  или writer.writerows(data)
    #     writer.writerow(row)

'''==============================================TASKS================================================'''
def honest_sellers_in_order():
    with open("csv_unit/sales.csv", "r", encoding="utf-8") as input_file:
        data = list(csv_unit.reader(input_file, delimiter=';'))[1:]
        honest_sales =filter(lambda line: int(line[2]) < int(line[1]), data)
        return "\n".join([line[0] for line in honest_sales])
def average_salary_in_order():
    with open("csv_unit/salary_data.csv", "r", encoding="utf-8") as input_file:
        data = list(csv_unit.reader(input_file, delimiter=";"))[1:]
        new_dict, new_dict_h = {}, {}
        for line in data:
            new_dict_h[line[0]] = new_dict_h.get(line[0], 0) + 1
            new_dict[line[0]] = new_dict.get(line[0], 0) + int(line[1])
        total = {key:new_dict[key]/new_dict_h[key]  for key in new_dict.keys()}
        return "\n".join(sorted(total, key=lambda value: (int(total[value]), value)))

def deniro_1(num):
    with open("csv_unit/deniro.csv", "r", encoding="utf-8") as input_file:
        data = list(csv_unit.reader(input_file, delimiter=','))
        if num == 1:
            data = sorted(data, key=lambda line: line[0])
        else:
            data = sorted(data, key=lambda line: int(line[num-1]))
        # [print(line) for line in data]
        return "\n".join([",".join(line) for line in data])

def csv_columns(filename):
    with open(filename, "r", encoding="utf-8") as input_file:
        data = [line for line in csv_unit.DictReader(input_file, delimiter =",")]
        new_dict = {}
        for line in data:
            for key in line:
                new_dict.setdefault(key, []).append(line[key])
        return data

def popular_domain():
    with open("csv_unit/data.csv", "r", encoding="utf-8") as input_file,\
            open("csv_unit/domain_usage.csv", "w", encoding="utf-8", newline="") as output_file:

        data = [line[2] for line in list(csv_unit.reader(input_file, delimiter=','))[1:]]
        domain_list, domain_dict = [data[i][data[i].index("@")+1:] for i in range(len(data))], {}
        for domain in domain_list:
            domain_dict[domain] = domain_dict.get(domain, 0) + 1
        total = sorted([{"domain":domain, "count":domain_dict[domain]} for domain in domain_dict],
                       key=lambda line: (line["count"], line["domain"]))
        head = ["domain", "count"]
        writer = csv_unit.DictWriter(output_file, fieldnames=head, delimiter=',')
        writer.writeheader()
        for row in total:
            writer.writerow(row)
        return None

def moscow_wifi():
    with open("csv_unit/wifi.csv", "r", encoding="utf-8") as input_file:
        data = [[line[1], int(line[3])] for line in list(csv_unit.reader(input_file, delimiter=";"))[1:]]
        new_dict = {}
        for line in data:
            new_dict[line[0]] = new_dict.get(line[0], 0) + line[1]
        return "\n".join([f"{key}: {value}" for key, value in sorted(new_dict.items(), key=lambda line: (-line[1], line[0]), reverse=False)])

def last_day_on_titanic():
    with open("csv_unit/titanic.csv", "r", encoding="utf-8") as input_file:
        data = list(filter(lambda line: line["survived"] == "1" and  float(line["age"]) < 18, [line for line in csv_unit.DictReader(input_file, delimiter=";")]))
        male_data = [dt["name"] for dt in list(filter(lambda line: line["sex"] == "male", data))]
        female_data = [dt["name"] for dt in list(filter(lambda line: line["sex"] == "female", data))]
        total = male_data + female_data
        return "\n".join(total)

def work_with_logs():
    with open("csv_unit/name_log.csv", "r", encoding="utf-8") as input_file, \
        open("csv_unit/new_name_log.csv", "w", encoding="utf-8", newline="") as output_file:
        data = list(csv_unit.reader(input_file, delimiter=","))
        head = data[0]
        new_dict = {line[1]:[] for line in data[1:]}
        for line in data[1:]:
            new_dict[line[1]] = new_dict.get(line[1], []) + [[line[0], datetime.strptime(line[2], "%d/%m/%Y %H:%M")]]
        for key in new_dict.keys():
            maximum, ind = new_dict[key][0][1], 0
            for i in range(len(new_dict[key])):
                if maximum <= new_dict[key][i][1]:
                    maximum = new_dict[key][i][1]
                    ind = i
                else:
                    continue
            new_dict[key] = new_dict[key][ind]
        writer = csv_unit.DictWriter(output_file, fieldnames=head, delimiter=',')
        writer.writeheader()
        total = [
            {"username": new_dict[key][0], "email": key, "dtime": datetime.strftime(new_dict[key][1],"%d/%m/%Y %H:%M" )} for key in new_dict.keys()
        ]
        for row in sorted(total, key=lambda line: line["email"]):
            writer.writerow(row)
        return new_dict


def condense_csv(filename, id_name):
    with open(filename, "r", encoding="utf-8") as input_file, \
        open("csv_unit/condensed.csv", "w", encoding="utf-8", newline="") as output_file:
        data = list(csv_unit.reader(input_file))
        head = list(set(line[0] for line in data))
        new_dict, total = {}, []
        for h in head:
            for line in data:
                if h == line[0]:
                    new_dict.setdefault(h, {}).update({line[1]:line[2]})
        total_head = [id_name] + [key for key in [new_dict[key] for key in new_dict.keys()][0].keys()]

        writer = csv_unit.writer(output_file, delimiter=',')
        writer.writerow(total_head)
        for key in sorted(new_dict.keys()):
            total.append([key] + [key for key in new_dict[key].values()])
        for row in total:
            writer.writerow(row)
        return True

def growth_of_classes():
    with open("csv_unit/student_counts.csv", "r", encoding="utf-8") as input_file, \
            open("csv_unit/sorted_student_counts.csv", "w", encoding="utf-8", newline="") as output_file:
        data = [line for line in csv_unit.DictReader(input_file, delimiter =",")]
        head = ["year"] + sorted(list(data[0])[1:], key=lambda i: (int(i[0:-2]), i[-1]))
        years = [line["year"] for line in data]
        for ind_i in range(len(data)):
            data[ind_i].pop("year")
            amount = [data[ind_i][key] for key in sorted(data[ind_i].keys(), key=lambda i: (int(i[0:-2]), i[-1]))]
            years[ind_i] = [years[ind_i]] + amount
        writer = csv_unit.writer(output_file, delimiter=',')
        writer.writerow(head)
        for row in years:
            writer.writerow(row)
        return True

def hungry_student():
    with open("csv_unit/prices.csv", "r", encoding="utf-8") as input_file:
        data = [line for line in csv_unit.DictReader(input_file, delimiter =";")]
        shops, new_dict = [line["Магазин"] for line in data], {}
        for i in range(len(data)):
            data[i].pop("Магазин")
            new_dict.setdefault(shops[i], min(data[i].items(), key=lambda x: int(x[1])))
        iskomy_prouct = sorted(new_dict.items(), key=lambda line: (int(line[1][1]), len(line[1][0])))[0]
        return f"{iskomy_prouct[0]}: {iskomy_prouct[1][0]}"