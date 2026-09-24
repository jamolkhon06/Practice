'''
LIST:
    1. Working with lists
    2. List methods
    3. Lambda function
    4. enumerate, map and filter
'''
print("_____Working with lists_____")
# Java/PHP, NodeJS => Python list, array

# literal
person = {"name": "Joseph", "age": 20}
people = ("Andrew", "John", "Michael")
groups = ["MIT", 'FLEXY', "DEVEX", "MG"]
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello world")
print(f"the result: {result} and size: {len(result)}")

fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print(a)
print(b)
print(c)
print(d)

print("_____List methods_____")
# methods > append(), insert(), pop(), remove(), clear(), sort(), index()

letters = ["a", "d", "b"]
letters.append("c")  # oxiridan qo'shib beradi
letters.insert(0, "z")  # xohlagan joyimizga ma'lumot qo'shsak bo'ladi

size = len(letters) - 1
result1 = letters.pop(size)  # oxirgisini o'chirib beradi
print(f"the pop result: {result1} and letters: {letters}")

result2 = letters.pop(0)  # old qismidan ma'lumotni o'chirib beradi
print(f"the pop result: {result2} and letters: {letters}")

print("_______")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print(animals)

animals.remove("lion")
print(animals)

del animals[2:4]
print(animals)

exist = animals.index("cat")
print(exist)

animals.clear()
print(animals)

if "cat" in animals:
    print("Index of cat:", animals.index("cat"))
else:
    print("Cat does not exist")

print("_____")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# immutable > sorted(), index()
nums = [2, 20, 12, 100]
new_nums = sorted(nums)
print(new_nums)


print("_____Lambda functions_____")
# lambda is small anonymous function!
def calculate(x, y): return x * y


result3 = calculate(3, 5)
print(result3)

peoples = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Micheal", 30)
]
# sort by age via lambda
peoples.sort(key=lambda person: person[1])
print(peoples)


print("_____enumerate, map and filter_____")
# enumerate for index & value

animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print(element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")


# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)
result4 = car_obj.items()
print(result4)
for (key, value) in result4:
    print(f"the key: {key} and value: {value}")

print("_____")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
new_cars = []
for car in cars:
    new_cars.append(car[0])
print(new_cars)

result5 = map(lambda car: car[0], cars)
print(result5)

new_car = list(result5)
print(new_car)

print("_____")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(result_filter)
print(list(result_filter))
