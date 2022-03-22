class Circle:
    __pi = 3.14

    def __init__(self, diameter):  # only receive one parameter - its diameter
        self.diameter = diameter
        self.radius = self.diameter / 2  # => so we need to find the radius for the formulas


    def calculate_circumference(self):  # 2 * pi * r  => so we need to find the radius
        return 2 * self.__pi * self.radius

    def calculate_area(self):  # pi * r * r
        return self.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):  # (angle / 360) * pi * r * r
        return (angle / 360) * self.__pi * self.radius ** 2

circle = Circle(10)  # Submit only the class, whithout the given variables: circle and angle
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
