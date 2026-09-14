'''
CLASS
    1. What is Class
    2. ordinary vs static properties
    3. special/magic methods
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


print("_____special/magic methods_____")
# Python's most special methods
# __init__, __new__, __str__, __call__, __getItem__, __eq__, __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"The {self.name} started engine")

    def stop_engine(self):
        print(f"The {self.name} stopped engine")

    def __str__(self):
        return f"The car.name: {self.name} was produced in {self.year}"

    def __call__(self):
        print("Object was called as a function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

your_car = Car("Toyota", 2026)
print(your_car)
response = your_car()
print(response)
