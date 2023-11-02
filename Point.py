
class Point:
    def __init__(self, x, y):
        self._x = x  # Initialize the x-coordinate of the Point
        self._y = y  # Initialize the y-coordinate of the Point

    @property
    def x(self):
        return self._x  # Getter method for the x-coordinate

    @x.setter
    def x(self, value):
        self._x = value  # Setter method for the x-coordinate

    @property
    def y(self):
        return self._y  # Getter method for the y-coordinate

    @y.setter
    def y(self, value):
        self._y = value  # Setter method for the y-coordinate

    def move(self, new_x, new_y):
        self._x = new_x  # Move the Point to a new x-coordinate
        self._y = new_y  # Move the Point to a new y-coordinate

    def __str__(self):
        return f"({self._x}, {self._y})"  # String representation of the Point

