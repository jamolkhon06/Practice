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


print("_____Condition_____")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("_____")

age = 18
""" person = None
if age > 16:
    person = "adult"
else:
    person = "child"
print(person) """

# Ternary operators
person = "adult" if age >= 18 else "minor"
print(person)

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, do you want to be student?")
elif is_admin:
    print("Please go to this office!")
elif is_guest or is_parent:
    print("Waiting room is over there")
else:
    print("Other cases")
