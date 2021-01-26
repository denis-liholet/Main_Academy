# Создать словарь, где ключ - значение списка users,
# значение - значение списка marks
# Использовать встроенную в python функцию zip
# result = {'Ann': 5, 'Jane': 4, 'Bob': 3, 'Bill': 4, 'John': 5}

users = ["Ann", "Jane", "Bob", "Bill", "John"]
marks = [5, 4, 3, 4, 5]


new_dict = {}
for i, j in zip(users, marks):
    new_dict[i] = j
print(new_dict)
