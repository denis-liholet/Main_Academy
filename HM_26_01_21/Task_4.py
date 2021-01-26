# Создать список, содержащий общие для двух данных списков числа

list_1 = [1, 2, 3, 4, 2]
list_2 = [2, 4, 6, 8, 2]
temp_lst = []

for item in list_1:             # remove duplicates from List_1
    if item not in temp_lst:
        temp_lst.append(item)

new_lst = [item for item in temp_lst if item in list_2]
print(new_lst)
