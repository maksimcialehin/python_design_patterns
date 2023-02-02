from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x=}, {self.y=}'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = PointFactory.new_cartesian_point(2, 3)
    p2 = PointFactory.new_polar_point(1, 2)

    print(p)
    print(p2)
