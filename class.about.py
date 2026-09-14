'''
CLASS
    1. What is Class
    2. ordinary vs static properties
    3. special methods
'''
print("_____What is Class?_____")
# class => blueprint for object creation!
# structure => state, constructor, and method


class Person():
    # state
    message = "static state property"

    # consturctor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I am {self.age} years old!")

    @classmethod
    def explain(self):
        print("Class: static method property executed")


person1 = Person("Joseph", 20)
person2 = Person("Justin", 25)
person3 = Person("John", 22)

# ordinary state property
print(person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("_____ordinary vs static properties_____")
# static state
new_message = Person.message
print(new_message)

# static method
Person.explain()
