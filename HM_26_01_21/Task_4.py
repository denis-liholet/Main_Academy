# Создать список, содержащий общие для двух данных списков числа

list_1 = [1, 2, 3, 4]
list_2 = [2, 4, 6, 8]

new_lst = [item for item in list_1 if item in list_2]
print(new_lst)
