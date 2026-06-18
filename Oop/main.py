
class Factory:
    # constructor(for accepting parameters)
    # self targets the location of called obj in the RAM.
    def __init__(self, material, zips, pockets):  #this is dender method as it has underscores
        self.material = material
        self.zips = zips
        self.pockets = pockets 

    def show(self):
        print(f"your object details are {self.material}, {self.pockets}, {self.zips}")

    @classmethod
    def hello(cls):
        print("Hello cls points out the location of the class")

reebok = Factory("leather", 3,2)

campus = Factory("leather", 3,2)

reebok.show()