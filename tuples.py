'''
TUPLE:
    1. What is tuple: typle vs list
    2. Unpacking arguments
    3. zip
'''
print("_____What is tuple: typle vs list_____")
# Java/PHP, NodeJS => Python list, array

# literal
nums = [3, 5, 1, 2]
car_dict = {"brand": "Ferrari", 'year': 1995}

# constructor
letters = list('Hello world')
person = dict(name="Joseph", age=20)

fruits = ["apple", "lemon", "banana", "kiwi"]
print(fruits)
fruits[2] = "melon"
print(fruits)

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"
