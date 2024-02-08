n = int(input())
my_list0, my_list1= [], []

for i in range(n):
    my_list0.append(int(input()))

del my_list0[my_list0.index(min(my_list0))]
del my_list0[my_list0.index(max(my_list0))]
print(*my_list0, sep='\n')


