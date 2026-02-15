class Flyer:
    def fly(self, height):
        return f"Flying at {height} meters"

class Camera:
    def take_photo(self, location):
        return f"Photo taken at {location}"

class Drone(Flyer, Camera):
    pass

d1 = Drone()
print( d1.fly(50))
print( d1.take_photo("mountain"))
print( d1.fly(0))
print( d1.take_photo("river"))