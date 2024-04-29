import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle sides")
    def is_valid_triangle(self):
        return (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b)

    def get_sides(self):
        return self.a, self.b, self.c

    def get_perimetr(self):
        return f"Triangle perimetr is  {self.a + self.b + self.c} "

    def get_area(self):
        p = self.a + self.b + self.c
        return f"Triangle area is {round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 2)}"

    def is_equalateral(self):
        return self.a == self.b == self.c

    def is_isoceles(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def is_right(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or self.b ** 2 + self.c ** 2 == self.a ** 2

    def is_isosceles(self):
        return self.a != self.b != self.c

    def get_angle(self):
        return f" Triangle angle are {math.acos(self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)},{math.acos(self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)},{math.acos(self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)}"

    def get_inradius(self):
        return f" Triangle inradius is {self.get_area() / (self.get_perimetr() / 2)}"

    def get_circumradius(self):
        return f"Triangle circumradius is {self.a / (2 * self.get_angle())}"


triangle1 = Triangle(2, 3, 4)
print(triangle1.is_valid_triangle())
print(triangle1.is_isoceles())
print(triangle1.is_isosceles())
print(triangle1.is_equalateral())
print(triangle1.is_right())

print(triangle1.get_perimetr())
print(triangle1.get_area())
print(triangle1.get_angle())
print(triangle1.get_inradius())
print(triangle1.get_circumradius())
