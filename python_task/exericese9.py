class vehical:
    def __init__(self, make, model,colour):
        self.make = make
        self.model = model
        self.colour = colour

class Car(vehical):
    def __init__(self, make, model, num_doors,colour):
        super().__init__(make, model,colour)
        self.num_doors = num_doors
        self.colour = colour

    def show_details(self):
        print("make:", self.make)
        print("model:", self.model)
        print("number of doors:", self.num_doors)
        print("colour :",self.colour)

my_car = Car("shift", "2025", 4, "red")
my_car.show_details()
 
