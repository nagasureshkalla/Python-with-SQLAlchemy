
class Circle:
    def __init__(self, radius, point):
        self._radius = radius  # Initialize the radius of the Circle
        self._point = point    # Initialize the center point of the Circle (a Point object)

    @property
    def radius(self):
        return self._radius  # Getter method for the radius

    @radius.setter
    def radius(self, value):
        self._radius = value  # Setter method for the radius

    def move(self, new_x, new_y):
        self._point.move(new_x, new_y)  # Move the Circle by moving its center Point

    def __str__(self):
        return f"A circle with radius {self._radius} center point {self._point}"  # String representation of the Circle
