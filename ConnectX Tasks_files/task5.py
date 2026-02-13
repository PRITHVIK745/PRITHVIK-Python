class User:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


class Driver(User):
    def __init__(self, car, **kwargs):
        self.car = car
        super().__init__(**kwargs)


class Rider(User):
    def __init__(self, pickup_location, **kwargs):
        self.pickup_location = pickup_location
        super().__init__(**kwargs)


class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        super().__init__(name=name, car=car, pickup_location=pickup_location)

    def summary(self):
        return f"{self.name} will pick up the rider from {self.pickup_location} using {self.car}."


t1 = Trip("Amit", "Honda City", "Sector 21")
print(t1.summary())