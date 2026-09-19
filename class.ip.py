print("_____INHERITANCE_____")
# Parent > Child[only public & protected properties(state + method)]


class Animal(object):
    # state
    description = "This class is parent for all animals"

    # constructor

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

    def make_voice(self):
        print(f"The {self.name} says {self.sound}")


class Cat(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("_____")
dog.make_voice()
fish.make_voice()

print("_____")
print(Animal.description)
print(Cat.description)
print("status:", dog.status)


print("_____POLYMORPHISM_____")
dog.make_voice()
fish.make_voice()


print("_____")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
result = a and b and c
print(result)


# fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print(data1, data2)
