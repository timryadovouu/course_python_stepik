from math import *
from datetime import datetime
with open('files.txt', encoding='utf-8') as in_file:
    my_list = list(map(lambda line: line.strip().split(), in_file.readlines()))
    my_dict = {}
    for item in my_list:
        ind = item[0].index(".")
        file_extension = item[0][ind+1:]
        my_dict.setdefault(file_extension)

    for key in my_dict:
        fe = []
        fv = []
        fv_d = {}
        for item in my_list:
            ind = item[0].index(".")
            if key == item[0][ind+1:]:
                fe.append(item[0])
                item[1] = int(item[1])
                if item[2] == "KB":
                    item[1] *= 1024
                if item[2] == "MB":
                    item[1] *= 1024**2
                if item[2] == "GB":
                    item[1] *= 1024**3
                fv.append(item[1])
        summa = sum(fv)
        # print(fv)
        f_ex =["B", "KB", "MB", "GB"]
        b_ind = 0
        while summa // 1024 != 0:
            summa /= 1024
            b_ind += 1
        my_dict[key] = fe, round(summa), b_ind
out_file = open('../ou.txt', 'w', encoding='utf-8')
for key in dict(sorted(my_dict.items())):
    for item in sorted(my_dict[key][0]):
        print(item)
        out_file.write(f"{item}\n")
    print("----------", f"Summary: {my_dict[key][1]} {f_ex[my_dict[key][2]]}","", sep='\n')
    x = ["----------\n", f"Summary: {my_dict[key][1]} {f_ex[my_dict[key][2]]}\n","\n"]
    out_file.writelines(x)
out_file.close()
