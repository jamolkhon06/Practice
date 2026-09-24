'''
Array & Set
    1. Array
    2. Set
    3. Specific operators with set
'''
from array import array
# i[integer], f[float]
print("_____Array_____")
numbers = array("i", [1, 4, 5, 7, 8, 41])

numbers.append(100)
numbers.insert(0, 14)
print(numbers)

numbers.remove(5)
numbers.pop()
print(numbers)

del numbers[0:2]
print(numbers)


print("_____Set_____")
# set of unique collection without keeping order
new_numbers = array("i", [1, 4, 7, 5, 7, 5, 4, 7, 8, 4, 41])
nums_set = set(new_numbers)
print(nums_set)

nums_set.add(200)
print(nums_set)

nums_set.add(7)
print(nums_set)

print("_____Specific operators with set_____")
# | & - ^

a = {10, 20, 30}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symetric difference
print(result4)
