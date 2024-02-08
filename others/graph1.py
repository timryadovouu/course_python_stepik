import matplotlib.pyplot as plt
import numpy as np

class Draw:
    def __init__(self, euler, heun, rk4, real):
        self.flag_euler = bool(int(euler))
        self.flag_heun = bool(int(heun))
        self.flag_rk4 = bool(int(rk4))
        self.flag_real = bool(int(real))
        self._x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # область определения
        self.x_1 = [np.cos(2 * x) - 0.5 * np.sin(2 * x) for x in self._x]  # эталон первой функции
        self.x_2 = [-2 * np.sin(2 * x) - np.cos(2 * x) for x in self._x]  # эталон второй функции

        self.euler_x_1,  self.euler_x_2 = [], []
        self.heun_x_1,  self.heun_x_2 = [], []
        self.rk4_x_1,  self.rk4_x_2, self.k_dict, self.l_dict = [], [], {}, {}

    def euler(self):
        self.euler_x_1 = [1]
        self.euler_x_2 = [-1]
        for pair in enumerate(self._x[:len(self._x) - 1], start=1):
            self.euler_x_1.append(round(self.euler_x_1[pair[0] - 1] + 0.1 * self.euler_x_2[pair[0] - 1], 3))
            self.euler_x_2.append(round(self.euler_x_2[pair[0] - 1] - 0.4 * self.euler_x_1[pair[0] - 1], 3))

        plt.plot(self._x, self.euler_x_1, color="red", marker="o", label="euler_x1")
        plt.plot(self._x, self.euler_x_2, color="red", marker="o", label="euler_x2")

    def heun(self):
        self.heun_x_1 = [1]
        self.heun_x_2 = [-1]
        for pair in enumerate(self._x[:len(self._x) - 1], start=1):
            self.heun_x_1.append(
                round(self.heun_x_1[pair[0] - 1] + 0.1 * 0.5 * (2 * self.heun_x_2[pair[0] - 1] - 0.4 * self.heun_x_1[pair[0] - 1]), 3))
            self.heun_x_2.append(round(self.heun_x_2[pair[0] - 1] + 0.1 * 0.5 * (
                    -4 * self.heun_x_1[pair[0] - 1] - 4 * (self.heun_x_1[pair[0] - 1] + 0.1 * self.heun_x_2[pair[0] - 1])), 3))

        plt.plot(self._x, self.heun_x_1, color="blue", marker="o", label="heun_x1")
        plt.plot(self._x, self.heun_x_2, color="blue", marker="o", label="heun_x2")

    def rk4(self):
        self.rk4_x_1 = [1]
        self.rk4_x_2 = [-1]
        self.k_dict = {"k1": [], "k2": [], "k3": [], "k4": []}
        self.l_dict = {"l1": [], "l2": [], "l3": [], "l4": []}
        for pair in enumerate(self._x, start=1):
            self.k_dict["k1"].append(0.1 * self.rk4_x_2[pair[0] - 1])
            self.l_dict["l1"].append(-0.4 * self.rk4_x_1[pair[0] - 1])

            self.k_dict["k2"].append(0.1 * (self.rk4_x_2[pair[0] - 1] + self.l_dict["l1"][pair[0] - 1] / 2))
            self.l_dict["l2"].append(-0.4 * (self.rk4_x_1[pair[0] - 1] + self.k_dict["k1"][pair[0] - 1] / 2))

            self.k_dict["k3"].append(0.1 * (self.rk4_x_2[pair[0] - 1] + self.l_dict["l2"][pair[0] - 1] / 2))
            self.l_dict["l3"].append(-0.4 * (self.rk4_x_1[pair[0] - 1] + self.k_dict["k2"][pair[0] - 1] / 2))

            self.k_dict["k4"].append(0.1 * (self.rk4_x_2[pair[0] - 1] + self.l_dict["l3"][pair[0] - 1]))
            self.l_dict["l4"].append(-0.4 * (self.rk4_x_1[pair[0] - 1] + self.k_dict["k3"][pair[0] - 1]))
            if pair[0] == len(self._x):
                # пропуск 12го значения
                continue
            self.rk4_x_1.append(round(self.rk4_x_1[pair[0] - 1] + 1 / 6 * (
                    self.k_dict["k1"][pair[0] - 1] + 2 * self.k_dict["k2"][pair[0] - 1] + 2 * self.k_dict["k3"][pair[0] - 1] +
                    self.k_dict["k4"][pair[0] - 1]), 3))
            self.rk4_x_2.append(round(self.rk4_x_2[pair[0] - 1] + 1 / 6 * (
                    self.l_dict["l1"][pair[0] - 1] + 2 * self.l_dict["l2"][pair[0] - 1] + 2 * self.l_dict["l3"][pair[0] - 1] +
                    self.l_dict["l4"][pair[0] - 1]), 3))

        plt.plot(self._x, self.rk4_x_1, color="orange", marker="o", label="rk4_x1")
        plt.plot(self._x, self.rk4_x_2, color="orange", marker="o", label="rk4_x2")

    def relative_error_calculation(self, a1, a2):
        result = 100*sum((a2[i]-a1[i])/a1[i] for i in range(len(self._x)))/len(self._x)
        return f"{round(abs(result), 3)}%"

    def draw(self):
        if self.flag_euler:
            self.euler()
            print(f"Погрешность для x1 в методе Эйлера: {self.relative_error_calculation(self.euler_x_1, self.x_1)}")
            print(f"Погрешность для x2 в методе Эйлера: {self.relative_error_calculation(self.euler_x_2, self.x_2)}")
        if self.flag_heun:
            self.heun()
            print(f"Погрешность для x1 в методе Хойна: {self.relative_error_calculation(self.heun_x_1, self.x_1)}")
            print(f"Погрешность для x2 в методе Хойна: {self.relative_error_calculation(self.heun_x_2, self.x_2)}")
        if self.flag_rk4:
            self.rk4()
            print(f"Погрешность для x1 в методе Рунге-Кутта: {self.relative_error_calculation(self.rk4_x_1, self.x_1)}")
            print(f"Погрешность для x2 в методе Рунге-Кутта: {self.relative_error_calculation(self.rk4_x_2, self.x_2)}")
        if self.flag_real:
            plt.plot(self._x, self.x_1, color="green", marker="o", label="real_x1")
            plt.plot(self._x, self.x_2, color="green", marker="o", label="real_x2")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Численные методы')
        plt.legend()
        plt.grid(True)
        plt.show()
        return "Done!"


test = Draw(input("Показать численный метод Эйлера? (1 или 0): "),
            input("Показать численный метод Хойна? (1 или 0): "),
            input("Показать численный метод Рунге-Кутта? (1 или 0): "),
            input("Показать исходный график? (1 или 0): "))

print(test.draw())