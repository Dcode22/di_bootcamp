import math
class Circle:
    def __init__(self, radius: int | None = None, diameter: int | None = None):
        if radius is not None and diameter is not None:
            raise Exception("only enter either radius or diameter")
        if radius:
            self.radius = radius
            self.diameter = radius*2
        if diameter:
            self.radius = diameter/2
            self.diameter = diameter

        self.area = self.radius**2 * math.pi

    def __str__(self):
        return str({"radius": self.radius, "diameter":self.diameter, "area": self.area})

    def __add__(self, other: "Circle") -> "Circle":
        return Circle(radius=self.radius + other.radius)
    
    def __lt__(self, other: "Circle"):
        if self.radius < other.radius:
            return True
        else: 
            return False
        
    def __eq__(self, other: "Circle") -> bool:
        if self.radius == other.radius:
            return True 
        else: 
            return False
    
cookie = Circle(diameter=2)
appetizer_plate = Circle(diameter=7)
dinner_plate = Circle(diameter=10)
silicon_wafer = Circle(diameter=10)
pizza = Circle(diameter=18)
print(dinner_plate)
print(appetizer_plate)
print(appetizer_plate + dinner_plate)
print(appetizer_plate < dinner_plate)
print(appetizer_plate > dinner_plate)
print(dinner_plate == silicon_wafer)

circles = [dinner_plate, cookie, silicon_wafer, pizza, appetizer_plate]
circles.sort()
for circle in circles:
    print(circle)
        
        