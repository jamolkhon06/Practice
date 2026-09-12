'''
FUNCTIONS:
    (1): DEFINE vs CALL
    (2): Parameter vs Argument
    (3): Keyword & default arguments
    (4): Scope
'''
print("_____DEFINE(parameter) vs CALL(argument)_____")
# built in functions > print(), type()
# Function => a reusable block of code
# Instead of block {} in JAVA, Python uses indentation

# DEFINE


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi, {b}"


# CALL
result1 = greet("Jamolkhon")
print("result1", result1)

result2 = greeting("Joseph")
print("result2", result2)

print("_____Keyword & default arguments_____")
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"


# CALL
result3 = give_greet(name="Joseph", age=20)
print("result3", result3)

result4 = give_greet("John")
print("result4", result4)


print("_____SCOPE_____")
b = 100  # 3


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f'the c value: {c}')


calculate(5, 50)
