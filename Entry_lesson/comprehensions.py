#List comprehension

div = "-------------------------------------"
print(div)

input_list_values = [a for a in range(25)]
print(input_list_values)
print(div)

# create a list with numbers non divisible by 2
out = [i for i in input_list_values if i % 2 != 0]
print(out)
print(div)

# create a list with all numbers and square elements which are divisible by 2
output_values = [i**2 if i % 2 == 0 else i for i in input_list_values]
print(output_values)
print(div)

# make a set from list with numbers divisible by 3
output_set_values = {i for i in input_list_values if i % 3 == 0}
print(output_set_values)
print(div)

# Dict comprehension

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

# create a dict from list of dicts
# expected result: {1: 'Ann', 2: 'John', 3: 'Bob', 4: 'Bill', 5: 'Jane'}

new_dict = {items["id"] : items["name"] for items in students if items["id"] % 2 ==0}
print(new_dict)
print(div)