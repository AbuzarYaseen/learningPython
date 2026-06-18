class Animal:
    def __init__(self, name):
        pass
    name1 = "Lion"

class Human:
    def __init__(self, name, age):
        pass
    name2 = "Ali"

class Robots(Animal, Human):
    name3 = "Charli123"

obj = Robots()

print(obj.name1, obj.name2, obj.name3)