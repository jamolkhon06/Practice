'''
COMPREHENSION:
    1. What is comprehension & list comp.
    2. set and dictionary comp.
'''
print('_____What is comprehension & list comp._____')
# Commprehension acts like spread operator

''' Comprehension general syntax:
    1. *iterable
    2. <expression> for item in iterable
    3. <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # 1-version
print(id(list_numbers), id(numbers))

people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # 2-version
print(list_people)

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # 3-version
print(list_cars)
