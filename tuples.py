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

# try to avoid this
people = "Andrew", "John"
animal = "dog",

print("_____Unpacking arguments_____")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print(z)

# *args > tuple


def calculate(*args):
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"total value: {total}")
    return total


calculate(1, 7, 2, 3)


# **kwargs > dictionary
def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old")
    pass


introduce(name="Joseph", age=20)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


greeting("Hi", True, 10, name="John", age=22)


print("_____zip_____")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print(zipped)
result = list(zipped)
print(result)
