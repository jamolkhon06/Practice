'''
LOOP operators:
    1. for
    2. break/else
    3. while
'''

print("_____for loop_____")
# iterable objects > string dic tuple list range map filter
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(letter)
print("_____")

for number in numbs:
    print(number)
print("_____")

for x in range_obj:
    print(x)
print("_____")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")


print("_____break else_____")
for y in range(1, 20, 5):
    print(f"the y: {y}")
    if (y > 10):
        print("Reached break")
        break
else:
    print("Looped successfully")


print("_____while operator_____")
num = 40
while num > 0:
    num -= 10
    print(f"The number equals {num}")
print("_____")

count = 0
while True:
    count += 1
    z = int(input("Find number: "))

    if z == 41:
        print(f"You found the number in {count} steps")
        break
    else:
        print("Wrong, please find again!")
