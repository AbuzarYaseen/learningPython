class Animal:
    def sound(self):
        print("Animals make different sounds")


class Cat(Animal):
    # Cat gives its own version of sound().
    def sound(self):
        print("Cat says meow")


class Dog(Animal):
    # Dog gives its own version of sound().
    def sound(self):
        print("Dog says bark")


class Cow(Animal):
    # Cow gives its own version of sound().
    def sound(self):
        print("Cow says moo")


# Different objects are stored in one list.
animals = [Cat(), Dog(), Cow()]

# Same method call, but different output for each object.
for animal in animals:
    animal.sound()
