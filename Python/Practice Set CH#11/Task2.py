class Animals:
    pass
class Pets(Animals):
    pass
class Dog:
    @staticmethod
    def Bark():
        print("Woof Woof!")

d = Dog()
d.Bark()