class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

    def show(self):
        print(f"your object details are material = {self.material}, zips = {self.zips}")

class LHRFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips) 
        self.color = color

    def show(self):
        print(f"your object details are material = {self.material}, zips = {self.zips}, color = {self.color}")

class GUJFactory(Factory):
    def __init__(self, material, zips, pockets):
        super().__init__(material, zips)
        self.pockets = pockets

    def show(self):
        print(f"your object details are material = {self.material}, zips = {self.zips}, pockets = {self.pockets}")

obj1 = GUJFactory("Leather", 3, 4)
obj2 = LHRFactory("Rexin", 5, "Orange")


obj1.show()
obj2.show()