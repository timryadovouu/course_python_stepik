import matplotlib.pyplot as plt
import numpy as np
from sympy import *

'''x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]

for j in range(40):
    y = [i * 1.2 + 1 for i in y]
    plt.plot(x, y, '--')'''

y_1 = [0.01, 1.59, 2.43, 3.23, 3.74, 4.33, 4.74, 5.08, 5.4, 5.65, 5.89, 6.08, 6.27, 6.42, 6.52]  #U=y
y_2 = [6, 27.5, 69, 80, 85.6, 88, 89, 88, 92, 98, 90]
y_3 = [1.9, 1.7, 1.5, 1.3, 1.1, 0.9, 0.7, 0.5, 0.3, 0.1, 0]
x_1 = [13.85, 11.51, 10.26, 9.08, 8.33, 7.45, 6.86, 6.35, 5.88, 5.51, 5.15, 4.87, 4.59, 4.36, 4.22] #I=x
x = list(map(lambda c: c*(10**(3)), x_1))
y = list(map(lambda c: c*(10**(-3)), y_1))
plt.xlabel('f::Гц')
plt.ylabel('fi')
plt.plot(x_1, y_1, 'o-r', label='U(I)')
# plt.plot(x, y2, 'o-g', label='R')
plt.legend()
plt.show()
