import os

# print(os.name)
# print(os.environ)    #Получить сведения, которые касаются конфигурации компьютера
# print(os.getenv("TMP"))
# print(os.getcwd())     #рабочая директория
# os.chdir(r"D:\folder")   #изменение рабочей директории
# print(os.path.exists("D:/acronis"))  #проверка существования пути
# print(os.path.isfile("D:/acronis"))  #Проверить, является ли определенный объект файлом
# print(os.path.isdir("D:/acronis"))   #Проверить, является ли определенный объект директорией

# os.mkdir(r"D:\1folder\test")    #Создание директорий
# os.makedirs(r"D:\folder\first\second\third")  #создавать сразу несколько новых папок в неограниченном количестве

# os.remove(r"D:\test.txt")    #Удаление файлов и директорий
# os.rmdir(r"D:\folder")       #стереть из памяти папку, если пустая
# os.removedirs(r"D:\folder\first\second\third")    #Для быстрого удаления множества пустых папок

# os.startfile(r"D:\for_manim\test.txt")   #Запуск на исполнение

# print(os.path.basename("D:/test.txt"))   #получить его полное имя документа
# print(os.path.dirname("D:/folder/test.txt"))   #получить только путь к файлу, без самого названия объекта

# print(os.path.getsize("D:\\for_manim\\test.txt"))   #Вычисление размера байты

# os.rename(r"D:\folder", r"D:\catalog")    #Переименование
# os.renames(r"D:\folder\first\second", r"D:\catalog\one\two")

# print(os.listdir(r"D:\for_manim"))   #Содержимое директорий list
#аналог листдир
def scandir():
    with os.scandir("D:\\for_manim") as entries:
        for entry in entries:
            print(entry.name)
def get_all_dir_files():
    for root, directories, files in os.walk(r"D:\1folder"):
        print(root)
        for directory in directories:
            print(directory)
        for file in files:
            print(file)
    return True

# print(os.stat(r"D:\for_manim"))  #основные сведения об объекте

# print(os.path.split(r"D:\folder\test.txt"))   #легко разъединять путь к файлу и имя файла в различные строки
# print(os.path.join(r"D:\folder", "test.txt"))   #обратное действие