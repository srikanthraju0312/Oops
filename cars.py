class Porsche:
    def __init__(self, model, power):
        self.model = model
        self.power = power
    def spec(self):
        print(f"Hi I'm Porsche {self.model} and my power is {self.power}bhp")
    def country(self):
        print("I'm a German Machine")
        
class Toyota:
    def __init__(self, model, power):
        self.model = model
        self.power = power
    def spec(self):
        print(f"Hi I'm Toyota {self.model} and my power is {self.power}bhp")
    def country(self):
        print("I'm a Japanese Machine")
        
por = Porsche(911,380)
toy = Toyota("Supra",335)

for cars in (por,toy):
    cars.spec()
    cars.country()