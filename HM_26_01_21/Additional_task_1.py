# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
# Входная строка может содержать содержит цифры, пробелы и латинские буквы.
# Программа должна вывести в одну строчку в порядке возрастания все цифры,
# встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.
# Input -> Output:
# abc12cd34ef35 -> 3
# yrey424u3iou2315 -> 2 3 4
# qwerty123 -> NO

input_string = input()

# инициализация итогового списка
result_lst = []

# заполнение временного списка цифрами, испльзуя метод isdigit()
temp_lst = [symbol for symbol in input_string if symbol.isdigit()]

# заполнение итогового списка только теми цифрами,
# которые повторяются более 1 раза, используя метод count()
for i in temp_lst:
    count = temp_lst.count(i)
    if count > 1:
        result_lst.append(i)

result_lst = list(set(result_lst))
result_lst.sort()

if len(result_lst) == 0:
    print('NO')

for i in result_lst:
    print(i, end=' ')
