# Написать программу, которая создает список,
# содержащий длину каждого слова, длиннее чем переменная n
# использовать list comprehension

sentence = "Python is a programming language that lets you work quickly and integrate systems more effectively."


word_length = int(input())
new_lst = [item for item in sentence.split() if len(item) > word_length]


print(new_lst)
