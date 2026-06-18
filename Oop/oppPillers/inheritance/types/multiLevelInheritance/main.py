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

class GUJFactory(LHRFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

    def show(self):
        print(f"your object details are material = {self.material}, zips = {self.zips}, color = {self.color}, pockets = {self.pockets}")

obj = GUJFactory("Leather", 3, "Red", 4)


obj.show()