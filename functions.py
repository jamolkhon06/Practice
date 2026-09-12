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
