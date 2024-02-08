import shutil
import os
import sys
import pprint
import time
#https://egorovegor.ru/python-shutil/
def copy_0():
    # Метод shutil.copy
    path = "D:/1folder"
    print(os.listdir(path))
    source = 'D:/1folder/test_1.txt'
    destinationfile = "D:/1folder/test_1(copy).txt"
    shutil.copy(source, destinationfile)
    print(os.listdir(path))
    return True

def copy2(filename):
    #Метод copy2 поддерживает метаданные
    stat_info = os.stat(filename)
    print("SOURCE time (D:/1folder/test_1.txt):")
    print("\tMode: ", stat_info.st_mode)
    print("\tCreated: ", time.ctime(stat_info.st_ctime))
    print("\tAccessed: ", time.ctime(stat_info.st_atime))
    print("\tModified: ", time.ctime(stat_info.st_mtime))
    #shutil.copy2('D:/1folder/test_1.txt', 'D:/1folder/test_1(copy).txt')   #make a copy
    return True

def copyfile():
    shutil.copyfile('D:/1folder/test_1.txt', 'D:/1folder/test_1(copy).txt')
    return True

def copytree():
    shutil.copytree('D:/1folder', 'D:/1folder_copy')
    pprint.pprint(os.listdir('D:/1folder_copy'))
    return True

def rmtree():
    #удалить папку
    shutil.rmtree('D:/1folder/test0')
    return True

def which():
    #поиск файлов
    return shutil.which("1_work_with_csv.py")     #не понятно

def disk_usage():
    total, used, free = shutil.disk_usage("d:/")
    gb = 1024**3
    print(round(total/gb))
    print(used/gb)
    print(free/gb)
    return True

def move():
    os.mkdir("D:/1folder/test")
    shutil.move("D:/1folder/test_1(copy).txt", "D:/1folder/copy_folder/")
    return True

def archive():
    #создание архива в корневом каталоге
    directory = "named_folder"
    shutil.make_archive("test_archive", "zip", directory)
    return True
    #все форматы
    # return shutil.get_archive_formats()

def archive_formats():
    return shutil.get_archive_formats()
print(archive_formats())