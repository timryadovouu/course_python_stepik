from math import *
def pascal(n):
    for q in range(n):
        my_list = [int((factorial(q))/(factorial(i)*factorial(q-i))) for i in range(0,q+1)]
        my_list_str = [str(i) for i in my_list]
        s_str = ' '.join(my_list_str)
        print(' '*(n-q-1) + s_str)
pascal(int(input()))

from math import *
def pascal(n):
    my_list = [int((factorial(n))/(factorial(i)*factorial(n-i))) for i in range(0,n+1)]
    return my_list
print(*pascal(int(input())))
