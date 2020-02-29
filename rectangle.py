class Rectangle(object):
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

# breadth = 120cm, length = 160cm, 1 cm^2 = Rs 2000
# Note:
#

r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2 " % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))

