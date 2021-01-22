# создать список с именами студентов, если их ID есть в списке student_ids
# result = ['Ann', 'John', 'Bob', 'Bill']
students = [
    {
        "id": 1,
        "name": "Ann"
    },
    {
        "id": 2,
        "name": "John"
    },
    {
        "id": 3,
        "name": "Bob"
    },
    {
        "id": 4,
        "name": "Bill"
    },
    {
        "id": 5,
        "name": "Jane"
    }
]
student_ids = [1, 2, 3, 4, 6, 7]
result_list = []

temp_dict = {items["id"]: items["name"] for items in students}

for i in range(len(student_ids)):
    if student_ids[i] in temp_dict:
        result_list.append(temp_dict.get(student_ids[i]))
print(result_list)
