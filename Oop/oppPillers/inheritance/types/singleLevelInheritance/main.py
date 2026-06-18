# Inheritance

class Factory:  #parent/super class
    a= "hello, I'm an attribute mentioned inside Factory"
    def hello(self):
        print("hello, I'm a method mentioned inside Factory")

class Factory2(Factory):    #child/sub class
    pass


obj = Factory()
print(obj.a)

obj2 = Factory2()
print(obj2.a)

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your pet name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)  #super targets the parent class
        self.age = age

    def show(self):
        print(f"hello your pet name is {self.name}, and your age is {self.age}")

ani = Animal("Lion")
person1 = Human("Puppy", 23)



person1.show()

ani.show()