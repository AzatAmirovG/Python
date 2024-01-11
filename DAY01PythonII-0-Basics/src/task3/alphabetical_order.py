# Считай файл names.txt и посчитай вхождения всех имен (имя - сколько раз встречается),
# а также отсортируй имена в алфавитном порядке и запиши в файл sorted_names.txt
from collections import Counter

with open('../../materials/task3/names.txt', 'r') as file:
    list_names = file.read().splitlines()
    list_names.sort()
    new_list = [x.split()[0] for x in list_names]
    print(*new_list, sep="\n")
    my_dict = {i:new_list.count(i) for i in new_list}
    # list_names.sort()
    # my_dict = dict(sorted(my_dict.items()))
    # for i in list_names

            
    


with open('sorted_names.txt', 'w') as file:
    for i, j in my_dict.items():
        print(f"{i} - {j}", file=file)

# print(new_list)