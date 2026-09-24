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
