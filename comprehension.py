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

people = [("Robert", 21), ("Steve", 19), ("Tony", 25)]
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

print('_____set and dictionary comp._____')
nums = [1, 5, 4, 20, 4, 5, 1, 4]
set_nums = {*nums}
print(set_nums)

dict_people = {person[0]: person[1] for person in people}  # 2-version
print(dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # 3-version
print(dict_people2)
