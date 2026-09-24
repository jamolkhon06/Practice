'''
Array & Set
    1. Array
    2. Set
    3. 
'''
from array import array
# i[integer], f[float]
numbers = array("i", [1, 4, 5, 7, 8, 41])

numbers.append(100)
numbers.insert(0, 14)
print(numbers)

numbers.remove(5)
numbers.pop()
print(numbers)

del numbers[0:2]
print(numbers)
