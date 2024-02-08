from zipfile import ZipFile
from datetime import datetime
import json
import os.path

'''==============================================READ================================================'''
#zip_file = ZipFile('test.zip')         #просто открыть
def work_with_all_files():
    with ZipFile("test.zip", mode="r") as zip_file:
        # zip_file.printdir()       #files
        info = zip_file.infolist()
        print(info[6].file_size)             # размер начального файла в байтах
        print(info[6].compress_size)          # размер сжатого файла в байтах
        print(info[6].filename)              # имя файла
        print(info[6].date_time)            # дата изменения файла
        print(info[0].is_dir())            #проверка на тип файла ПАПКА
        info_1 = zip_file.namelist()       #список директорий и файлов
        last_file = zip_file.getinfo(info_1[-1])    # получаем информацию об отдельном файле
def work_with_certain_file():
    with ZipFile('test.zip') as zip_file:
        with zip_file.open('test/Разные файлы/astros.json') as file:
            print(file.read().decode("utf-8"))

'''==============================================WRITE================================================'''
def writing():               #можно еще через мод = "а"
    with ZipFile('archive.zip', mode='w') as zip_file:
        zip_file.write('0_entrance.py', 'first.py')  # первый аргумент - это имя файла
        # zip_file.write('lse.jpeg', 'lse1.jpeg')         # второй аргумент - это имя файла в архиве
        print(zip_file.namelist())

'''==============================================EXTRACT================================================'''
def extracting():
    with ZipFile('test.zip') as zip_file:
        zip_file.extract('test/Картинки/avatar.png')
        zip_file.extract('test/Программы/image_util.py')
        zip_file.extract('lse.jpeg')
        # zip_file.extractall()     #извлечь все
'''==============================================TASKS================================================'''

def how_many_files():
    with ZipFile("zip_unit/workbook.zip") as zip_file:
        counter = 0
        for file in zip_file.infolist():
            if not file.is_dir():
                counter += 1
        answer = [1 for file in zip_file.infolist() if not file.is_dir()]
        return sum(answer)

def before_after_volume():
    with ZipFile("zip_unit/workbook.zip") as zip_file:
        before = [file.file_size for file in zip_file.infolist()]
        after = [file.compress_size for file in zip_file.infolist()]
        answer = [f"Объем исходных файлов: {sum(before)} байт(а)", f"Объем сжатых файлов: {sum(after)} байт(а)"]
        return "\n".join(answer)

def best_compression():
    with ZipFile("zip_unit/workbook.zip") as zip_file:
        data = list(filter(lambda line: line.file_size != 0, [file for file in zip_file.infolist()]))
        return min(data, key=lambda line: line.compress_size/line.file_size).filename.split("/")[-1]

def files_after_certain_date():
    with ZipFile("zip_unit/workbook.zip") as zip_file:
        string = "2021-11-30 14:22:00"
        data = list(filter(lambda line: line.date_time >= (2021, 11, 30, 14, 22) and line.is_dir() != True, zip_file.infolist()))
        new_data = [line.filename.split("/")[-1] for line in data]
        return "\n".join(new_data)

def formed_output():
    with ZipFile("zip_unit/workbook.zip") as zip_file:
        names = sorted([[line.filename.split("/")[-1],
                         f"  Дата модификации файла: {datetime(*line.date_time)}",
                         f"  Объем исходного файла: {line.file_size} байт(а)",
                         f"  Объем сжатого файла: {line.compress_size} байт(а)",
                         ""] for line in zip_file.infolist() if not line.is_dir()], key= lambda line: line[0].split("/")[-1])
        [print(item) for line in names for item in line]
        return True

def writing_task():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
    with ZipFile('zip_unit/files.zip', mode="w") as zip_file:
        [zip_file.write(line, arcname=None) for line in file_names]

def write_to_zip_if():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
    with ZipFile('zip_unit/files.zip', mode="w") as zip_file:
        [zip_file.write(line, arcname=None) for line in file_names if os.path.getsize(line) <= 100]

def extract_this(zip_name, *args):
    with ZipFile(zip_name, mode="r") as zip_file:
        if not len(args):
            zip_file.extractall()
        else:
            for file in [line for line in zip_file.infolist()]:
                for search in args:
                    if search == file.filename.split("/")[-1]:
                        zip_file.extract(file)
    return True

def total_footballers():
    def is_correct_json(json_file):
        try:
            return json.load(json_file)
        except:
            return False

    def footballers():
        answer = []
        with ZipFile("zip_unit/data.zip", mode="r") as zip_file:
            for file in filter(lambda line: line[-5:] == ".json", [file.filename for file in zip_file.infolist()]):
                zip_file.extract(file)
                with open(file, encoding="utf-8") as input_file:
                    cor = is_correct_json(input_file)
                    if cor:
                        if cor["team"] == "Arsenal":
                            answer.append(f"{cor['first_name']} {cor['last_name']}")
        return "\n".join(sorted(answer, key=lambda line:(line[0], line[line.index(" ") + 1])))
    return footballers()
def correct_prefix(file_size):
    ind = 0
    while file_size // 1024 > 0:
        file_size /= 1024
        ind += 1
    return round(file_size), ind
def archive_structure():
    structure = []
    prefixes = ["B", "KB", "MB", "GB"]
    with ZipFile("zip_unit/desktop.zip", mode="r") as zip_file:
        for file in zip_file.infolist():
            if file.is_dir():
                prob = (file.filename.count("/") - 1)*"  "
                name = file.filename.split("/")
                structure.append(f"{prob}{name[-2]}")
                # print(file.filename)
            else:
                name = file.filename.split("/")[-1]
                size = correct_prefix(file.file_size)
                prob = (file.filename.count("/")) * "  "
                structure.append(f"{prob}{name} {size[0]} {prefixes[size[1]]}")

    return "\n".join(structure)