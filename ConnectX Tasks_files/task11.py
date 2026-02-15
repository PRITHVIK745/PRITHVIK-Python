class Book:
    def read_page(self, page):
        return f"Reading page {page}"

class BatteryPowered:
    def battery_status(self, level):
        return f"Battery at {level}%"

class EBookReader(Book, BatteryPowered):
    pass

e1 = EBookReader()
print( e1.read_page(10))
print( e1.battery_status("90"))
print( e1.read_page(0))
print( e1.battery_status("0"))