# C помощью list comprehension сгенерировать
# новый список только с позитивными целыми числами

numbers = [2, -2.4, 3.3, -1, 7, 12, -11, 9.5]


new_lst = [item for item in numbers if item > 0 and isinstance(item, int)]
print(new_lst)
