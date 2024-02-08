import calendar
import locale
import json
import sys
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
'''==================================================TASK1==========================================================='''
def summary_1():
    month_dict = {index:month for index, month in enumerate(list(calendar.month_name)[1:], start=1)}
    try:
        return month_dict[int(input())]
    except KeyError:
        return "Введено число из недопустимого диапазона"
    except:
        return "Введено некорректное значение"

def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data.setdefault(key, [element])
    return None

def try_to_read():
    try:
        file = open(input(), encoding="utf-8")
        try:
            text = file.read()
            return text
        finally:
            file.close()
    except:
        return "Файл не найден"

'''==================================================TASK2==========================================================='''

def summary_2():
    try:
        nums = [10, 5, 20, 25]
        print(nums[100])
    except (KeyError, IndexError) as err:  # записываем сгенерированное исключение в переменную err
        print(err)
        print(type(err))
    try:
        х = 1 / 0
    except Exception as err:
        print(err)

def get_weekday(number):
    week_dict = {index: month.title() for index, month in enumerate(list(calendar.day_name), start=1)}
    if type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    if number in week_dict:
        return week_dict[number]
    else:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

def get_id(names, name):
    if type(name) != str:
         raise TypeError('Имя не является строкой')
    elif name != name.title() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    else:
        new_names = list(filter(lambda line: line == line.title() and line.isalpha(), names))
        return len(new_names)+1

def try_to_read_json():
    try:
        file = open(input(), encoding="utf-8")
        try:
            text = file.read()
            return text
        except:
            return "Ошибка при десериализации"
        finally:
            file.close()
    except:
        return "Файл не найден"

def try_to_read_json_vol2():
    try:
        with open(input(), encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return 'Файл не найден'
    except ValueError:
        return 'Ошибка при десериализации'

'''==================================================TASK3==========================================================='''

def is_good_password(string):
    if string.isalpha() or len(string) < 9 or string == string.lower() or string == string.upper():
        return False
    else:
        return True

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password_vol2(string):
    try:
        q = 1 / (not len(string) < 9)
    except:
        raise LengthError
    try:
        q = 1 / (any(i.isalpha() for i in string) and any(i.islower() for i in string) and any(i.isupper() for i in string))
    except:
        raise LetterError
    try:
        q = 1 / any(i.isdigit() for i in string)
    except:
        raise DigitError
    return True

def is_good_password_vol3():
    for psswrd in [line.strip() for line in sys.stdin]:
        try:
            is_good_password_vol2(psswrd)
            return "Success!"
        except Exception as err:
            print(err)

print(is_good_password_vol3())