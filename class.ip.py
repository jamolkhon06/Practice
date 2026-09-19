print("_____INHERITANCE_____")
# Parent > Child[only public & protected properties(state + method)]


class Animal:
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
