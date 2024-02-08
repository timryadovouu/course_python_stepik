from math import *

def is_kv(n):
    x = ceil(sqrt(n))
    if x*x == n:
        return True
    else:
        return False
def triangle_nun(cout_m):
    global num
    cout_0 = 2
    start_num = 3
    while cout_0 < cout_m:
        cout_0 = 2
        num = sum([c for c in range(1, start_num + 1)])
        for i in range(2, ceil(sqrt(num))):
            if num % i == 0:
                cout_0 += 2
        if is_kv(num):
            cout_0 -= 1
        start_num += 1
    return num

print(triangle_nun(int(input())))