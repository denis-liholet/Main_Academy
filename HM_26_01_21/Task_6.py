# Refactor given program code:
#   - Put reusable code into the functions:
#       - First - to calculate days in year
#       - Second – to decide which planet year is bigger
#   - Put orbital_radius and orbital_speed together in same data structure
# Optional: add try/except handlers to avoid entering incorrect planet

import math

orbital_data = [
    {'planet': 'Mercury', 'orbital_radius': 58,   'orbital_speed': 47.87},
    {'planet': 'Venus',   'orbital_radius': 108,  'orbital_speed': 35.02},
    {'planet': 'Earth',   'orbital_radius': 150,  'orbital_speed': 29.78},
    {'planet': 'Mars',    'orbital_radius': 228,  'orbital_speed': 24.13},
    {'planet': 'Jupiter', 'orbital_radius': 778,  'orbital_speed': 13.07},
    {'planet': 'Saturn',  'orbital_radius': 1429, 'orbital_speed': 9.69},
    {'planet': 'Uranus',  'orbital_radius': 2871, 'orbital_speed': 6.81},
    {'planet': 'Neptune', 'orbital_radius': 4504, 'orbital_speed': 5.43}
]


def length_of_the_year(planet):
    try:
        current_planet = next(item for item in orbital_data if item['planet'] == planet)
    except StopIteration:
        print("Can`t find information for this planet")
        exit()
    else:
        orbital_radius = current_planet['orbital_radius'] * 1000000  # turning millions of kilometres to kilometres
        orbital_speed = current_planet['orbital_speed']
        planet_year = (2 * math.pi * orbital_radius / orbital_speed) / (60 * 60 * 24)  # converting to days
        return "The year is {} days on {}".format(int(planet_year), planet)


def length_compare(first_planet, second_planet):
    bigger_year = planet1 if first_planet > second_planet else planet2  # Looking which year is bigger
    return "The {} year is bigger".format(bigger_year)


planet1 = input("Planet 1: ")
print(length_of_the_year(planet1))
planet2 = input("Planet 2: ")
print(length_of_the_year(planet2))
print(length_compare(length_of_the_year(planet1).split()[3], length_of_the_year(planet2).split()[3]))
