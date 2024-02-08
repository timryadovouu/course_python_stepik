import csv
import matplotlib.pyplot as plt

def graph():
    with open("C://Users//timar//OneDrive//Рабочий стол//itmo//3сем//операционные_системы//lab6//all.csv", "r", encoding="utf-8") as file:
        data = list(csv.reader(file))[1:]
        time = [int(line[0]) for line in data]
        malloc = [float(line[1]) for line in data]
        calloc = [float(line[2]) for line in data]
        tc_malloc = [float(line[3]) for line in data]

    plt.xlabel('memory')
    plt.ylabel('time')
    plt.plot(time, malloc, color="blue", marker="o", label="malloc")
    plt.plot(time, calloc, color="green", marker="o", label="calloc")
    plt.plot(time, tc_malloc, color="red", marker="o", label="tc_alloc")
    plt.legend()
    plt.show()

graph()