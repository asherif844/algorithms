class Car:
    num_of_cars = 0

    def __ini__(self, make, model):
        self.make = make
        self.model = model

Car.num_of_cars += 3
print(Car.num_of_cars)