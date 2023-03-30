class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what i say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34)
c.speak()
d = Dog("Jill", 25)
d.speak()