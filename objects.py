'''
OBJECTS:
    1. What is an Object
    2. Iterable objects & RANGE
    3. DICTIONARY
    4. Error handling system
'''
import array
import math
from math import ceil, asin

print("_____What is an Object?_____")
# An object has state and method properties
# Everything is object in Python!

print(type('Hello world'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm => Functional programming & OOP
# OOP 4 Concepts: Abstraction | Encapsulation | Inheritance | Polimorphism
# ceil() berilgan argument sonni yuqori songa o'zgartirib beradi
result1 = ceil(97.7)
print(result1)

result2 = ceil(98.7)
print(result2)

print("_____Error handling system_____")
car_dic = dict(name="Toyota", year=2026, electric=True)

try:
    print("Passed here")
    a = car_dic.speed
    result = car_dic["origin"]
    print(result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
