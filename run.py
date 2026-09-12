# a = 100
# print("a:", a)
# message = "Hello, World!"
# print("message:", message)

message = "PYTHON: Everything is object"
print(message)

result = type(message)
print(result)

# Dunder => dubble underscore; __init__
'''
In Python there are builtin tools:
1. TYPES > int, float, string, dictionary, list
2. FUNCTIONS > print(), len(), input(), type(), str(), int()
3. CONSTANTS > True, False, None
'''
print(dir(__builtins__))
