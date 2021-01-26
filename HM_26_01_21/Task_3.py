# Найти все цифры от 1 до 1000, которые содержат в себе 3

new_lst = [item for item in [i for i in range(1, 1001)] if '3' in str(item)]
print(new_lst)
