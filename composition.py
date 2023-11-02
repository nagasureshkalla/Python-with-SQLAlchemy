
"""
HW 3
Problem 1
Author : Kalla Naga Suresh

"""

from Point import Point
from Circle import Circle

if __name__ == '__main__':
    p1 = Point(0, 0)       # Create a Point object at (0, 0)
    c1 = Circle(1, p1)    # Create a Circle object with radius 1 and center at p1
    print('Before the move')
    print(c1)              # Display Circle information before moving
    c1.move(1, 1)         # Move the Circle to a new center (1, 1)
    print('After the move')
    print(c1)              # Display Circle information after moving
