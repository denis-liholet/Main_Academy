div = "-------------------------------------"
print(div)

# Write a Python program to check a list is empty or not.

list_empty = []
list_data = ['1', '2', '3']
if len(list_empty) == 0:
    print("empty")
else:
    print("not empty")

if len(list_data) == 0:
    print("empty")
else:
    print("not empty")
print(div)

# написать программу, которая принимает список и делит на 3 списка, слова, цифры, смешанный.
lst = ["1", "2", "3", "33333", "white", "yellow", "red", "all123"]
lst_num = []
lst_str = []
lst_other = []

for lst_item in lst:
    if lst_item.isalpha():
        lst_str.append(lst_item)
    elif lst_item.isdigit():
        lst_num.append(lst_item)
    else:
        lst_other.append(lst_item)
print(str(lst) + "\n" + str(lst_num) + "\n" + str(lst_str) + "\n" + str(lst_other))
print(div)
