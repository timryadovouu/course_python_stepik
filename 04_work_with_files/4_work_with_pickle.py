import pickle, sys
'''==============================================SUMMARY================================================'''

def dump_load():
    obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
    with open('file.pkl', 'wb') as file:
        pickle.dump(obj, file)
    with open('file.pkl', 'rb') as file:     # используется файл полученный на предыдущем шаге
        obj = pickle.load(file)
        print(obj)
        print(type(obj))
    return True
def dumps_loads():
    obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
    binary_obj = pickle.dumps(obj)
    print(binary_obj)
    print(type(binary_obj))
    new_obj = pickle.loads(binary_obj)
    print(new_obj)
    return True

'''==============================================TASKS================================================'''

def lonely_function():
    with open(input(), "rb") as function:
        f = pickle.load(function)
    return f(*list(map(str.strip, sys.stdin)))

def filter_dump(filename, objects, typename):
    with open(filename, "wb") as file:
        total = list(filter(lambda item: type(item) == typename, objects))
        pickle.dump(total, file)
    return True

def total_sum(file, num):
    with open(file, "rb") as input_file:
        data = pickle.load(input_file)
        total = 0
        if type(data) == list:
            try:
                total = min(filter(lambda item: type(item) == int, data)) * max(filter(lambda item: type(item) == int, data))
            except:
                total = 0
        elif type(data) == dict:
            try:
                total = sum([key for key in filter(lambda item: type(item) == int, data)])
            except:
                total = 0
        if total == num:
            return "Контрольные суммы совпадают"
        else:
            return "Контрольные суммы не совпадают"

