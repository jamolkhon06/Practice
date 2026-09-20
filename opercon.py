'''
OPERATIONS & CONDITIONS
    1. Operations
    2. Condition
    3. Logical Operators
'''

print("_____Operations_____")
# + - > >= < <= == is /   // % += **

a = 19
b = 5

print(a > b)
print(a / b)
print(a * b)


result = a // b
left = a % b
print(f"The result: {result} and left: {left}")

a += 100
print(a)
print(b**2)


print("_____"*5)

c = dict(name="Joseph", age=20)
d = dict(name="Joseph", age=20)
e = c
print(c == d)
print(id(c), id(d))


data1 = c is d
data2 = c is e
print(data1)
print(data2)
