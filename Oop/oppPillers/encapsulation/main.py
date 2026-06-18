class Demo:
    def __init__(self):
        self.name = "Public Name"
        self._age = 21
        self.__salary = 50000

    def show(self):
        print("Inside the class")
        print("Public: ", self.name)
        print("Protected: ", self._age)
        print("Protected: ", self.__salary)


obj = Demo()
obj._age = 32
obj.show()