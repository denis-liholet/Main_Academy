# Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать.
# Программа получает на вход строку, состоящую из заглавных и строчных символов, цифр и знаков препинания.
# Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.
# Input -> Output:
# hello_world! -> helo_wrd!

original_string = input()
duplicate_lst = []  # список для символов с кол-вом вхождений в строку более 1 раза
result_string = ''

for symbol in original_string:
    count = original_string.count(symbol)  # считаем кол-во вхождений символа
    if count == 1:
        result_string = result_string + symbol
    if count > 1 and symbol not in duplicate_lst:  # если символ входит в строку более 1 раза
        duplicate_lst.append(symbol)               # добавляем его в список дубликатов duplicate_lst
        result_string = result_string + symbol

print(original_string + ' -> ' + result_string)
