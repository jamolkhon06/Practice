''' Packages & Debugging
        1. Python Packages & Core Package
        2. Package Manager & External Package
        3. Debugging
'''

from PIL import Image
import turtle

print("_____Python Packages & Core Package_____")
'''Python Packages/Modules: Core, File, and External'''
# Core Packages: https://docs.python.org/3/library

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

# turtle.done()

print("_____")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()

# with - Context manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print(your_content)


print("_____Package Manager & External Package_____")
'''Package managers:
    1. Python > pip | pipenv
    2. NodeJS > npm | yarn
    3. PHP > composer
    4. MacOS > brew
'''
# External package: https://pypi.org/

with Image.open("material/image.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
